import { useEffect, useState } from 'react';
import config from '../components/config.js';
import { useAuth } from '../components/AuthProvider.js';

function DeliveryStatus({ cart }) {
    const [status, setStatus] = useState(null);
    const [reason, setReason] = useState('');
    const { authState } = useAuth();

    useEffect(() => {
        const checkItemQuantity = (items) => {
            for (let item of items) {
                if (item.quantity <= 0) {
                    return false;
                }
            }
            return true;
        };

        const checkAgvStatus = (agvs) => {
            if (!Array.isArray(agvs)) {
                console.error('agvs is not an array');
                return;
            }

            let hasRD = false; // 'RD' 상태의 AGV가 존재하는지를 나타내는 변수
            let allMA = true; // 모든 AGV가 'MA' 상태인지를 나타내는 변수
            for (let agv of agvs) {
                if (agv.status === 'RD') {
                    hasRD = true;
                }
                if (agv.status !== 'MA') {
                    allMA = false;
                }
            }
        
            if (!hasRD && !allMA) {
                setReason('준비상태의 AGV가 없습니다. 배송이 오래 걸립니다.');
            }
        
            return hasRD || allMA; // 'RD' 상태의 AGV가 하나라도 있거나 모든 AGV가 'MA' 상태이면 true를 반환
        };

        const checkArmStatus = (items, arms) => {
            let faultyArms = []; // 고장난 Arm의 번호를 저장할 배열
            for (let item of items) {
                const locationNumber = item.location_number.split('-')[0]; // 상품의 위치에서 x 값을 추출
                const arm = arms.find(a => a.rack_number === parseInt(locationNumber) && a.status === 'MA'); // Arm을 찾음
                if (arm) { // Arm이 존재하고 상태가 'MA'인 경우
                    faultyArms.push(locationNumber); // 고장난 Arm의 번호를 추가
                }
            }
            if (faultyArms.length > 0) {
                const faultyArmString = faultyArms.join(', '); // 배열을 문자열로 변환하여 출력
                setStatus(false);
                setReason(`${faultyArmString}번 렉 고장 주문 불가능입니다.`);
                return false; // 주문 불가능
            }
            return true; // 모든 Arm이 정상이면 주문 가능
        };

        const fetchData = () => {
            fetch(`${config.baseURL}api/agv/`, {
                headers: {
                    'Authorization': `Token ${authState.token}`
                }
                })
                .then(response => response.json())
                .then(agvs => { console.log(agvs);
                    if (!checkAgvStatus(agvs)) {
                        setStatus(false);
                        setReason('준비상태의 AGV가 없습니다.');
                        return;
                    }
                    fetch(`${config.baseURL}api/arms/`, {
                        headers: {
                            'Authorization': `Token ${authState.token}`
                        }
                        })
                        .then(response => response.json())
                        .then(arms => {
                            if (!checkArmStatus(cart, arms)) {
                                setStatus(false);
                                return;
                            }

                            if (!checkItemQuantity(cart)) {
                                setStatus(false);
                                setReason('아이템의 수량이 0 이하입니다.');
                                return;
                            }

                            setStatus(true);
                        });
                });
        };

        const intervalId = setInterval(fetchData, 500);  //

        // 카트가 비어 있는지 확인하고 1초마다 상태를 업데이트하는 타이머 설정
        const checkCartEmpty = () => {
            if (cart.length === 0) {
                setStatus(false);
                setReason('카트가 비어 있습니다.');
            }
        };

        const emptyCartIntervalId = setInterval(checkCartEmpty, 500);  // 매 0.5초마다 카트가 비어 있는지 확인합니다.

        // 컴포넌트가 언마운트되거나 종속성이 변경될 때 인터벌을 정리합니다.
        return () => {
            clearInterval(intervalId);
            clearInterval(emptyCartIntervalId);
        };
    }, [cart, authState.token]);

    // 상태와 이유를 반환합니다.
    return { status, reason };
}

export default DeliveryStatus;

//import { useEffect, useState } from 'react';
//import config from '../components/config.js';
//import { useAuth } from '../components/AuthProvider.js';

//function DeliveryStatus({ cart }) {
//    const [status, setStatus] = useState(null);
//    const [reason, setReason] = useState('');
//    const { authState } = useAuth();

//    useEffect(() => {
        
//        const checkItemQuantity = (items) => {
//            for (let item of items) {
//                if (item.quantity <= 0) {
//                    return false;
//                }
//            }
//            return true;
//        };

//        const checkAgvStatus = (agvs) => {
//            if (!Array.isArray(agvs)) {
//                console.error('agvs is not an array');
//                return;
//            }

//            let hasRD = false; // 'RD' 상태의 AGV가 존재하는지를 나타내는 변수
//            let allMA = true; // 모든 AGV가 'MA' 상태인지를 나타내는 변수
//            for (let agv of agvs) {
//                if (agv.status === 'RD') {
//                    hasRD = true;
//                }
//                if (agv.status !== 'MA') {
//                    allMA = false;
//                }
//            }
        
//            if (!hasRD && !allMA) {
//                setReason('준비상태의 AGV가 없습니다. 배송이 오래 걸립니다.');
//            }
        
//            return hasRD || allMA; // 'RD' 상태의 AGV가 하나라도 있거나 모든 AGV가 'MA' 상태이면 true를 반환
//        };

//        const checkArmStatus = (items, arms) => {
//            let faultyArms = []; // 고장난 Arm의 번호를 저장할 배열
//            for (let item of items) {
//                const locationNumber = item.location_number.split('-')[0]; // 상품의 위치에서 x 값을 추출
//                const arm = arms.find(a => a.rack_number === parseInt(locationNumber) && a.status === 'MA'); // Arm을 찾음
//                if (arm) { // Arm이 존재하고 상태가 'MA'인 경우
//                    faultyArms.push(locationNumber); // 고장난 Arm의 번호를 추가
//                }
//            }
//            if (faultyArms.length > 0) {
//                const faultyArmString = faultyArms.join(', '); // 배열을 문자열로 변환하여 출력
//                setStatus(false);
//                setReason(`${faultyArmString}번 렉 고장 주문 불가능입니다.`);
//                return false; // 주문 불가능
//            }
//            return true; // 모든 Arm이 정상이면 주문 가능
//        };

//        fetch(`${config.baseURL}api/agv/`, {
//            headers: {
//                'Authorization': `Token ${authState.token}`
//            }
//            })
//            .then(response => response.json())
//            .then(agvs => { console.log(agvs);
//                if (!checkAgvStatus(agvs)) {
//                    setStatus(false);
//                    setReason('준비상태의 AGV가 없습니다.');
//                    return;
//                }
//                fetch(`${config.baseURL}api/arms/`, {
//                    headers: {
//                        'Authorization': `Token ${authState.token}`
//                    }
//                    })
//                    .then(response => response.json())
//                    .then(arms => {
//                        if (!checkArmStatus(cart, arms)) {
//                            setStatus(false);
//                            return;
//                        }

//                        if (!checkItemQuantity(cart)) {
//                            setStatus(false);
//                            setReason('아이템의 수량이 0 이하입니다.');
//                            return;
//                        }

//                        setStatus(true);
//                    });
//            });
//        fetch();
//        const intervalId = setInterval(fetch, 5000);  // 매 5초마다 데이터를 요청합니다.
//        // 컴포넌트가 언마운트되거나 종속성이 변경될 때 인터벌을 정리합니다.
//        return () => clearInterval(intervalId);
//    }, [cart, authState.token]);

//    // 상태와 이유를 반환합니다.
//    return { status, reason };
//}

//export default DeliveryStatus;
