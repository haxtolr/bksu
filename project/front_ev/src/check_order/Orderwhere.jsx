import { useAuth } from '../components/AuthProvider.js';
import { Button } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import config from '../components/config.js';

function Orderwhere() {
    const { authState } = useAuth();  // authState 가져오기
    const [orderData, setOrderData] = useState(null);
<<<<<<< HEAD
    const [progress, setProgress] = useState(0);
    const [targetProgress, setTargetProgress] = useState(0);
=======
      // 로그인한 사용자의 username 가져오기

    const progress = 1;
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127

    useEffect(() => {
        const fetchData = async () => {
            const username = authState.username;
            
            if (!username) return(console.error(authState.username));
            try {
                const response = await axios.get(`${config.baseURL}api/latest_order/${authState.username}/`, {
                    headers: {
                        'Authorization': `Token ${authState.token}`  // 토큰을 헤더에 추가
                    }
                });
                setOrderData(response.data);
<<<<<<< HEAD
                const location = response.data.agv.location;
                const newTargetProgress = parseInt(location.replace('%', ''), 10);
                setTargetProgress(newTargetProgress);  // setProgress는 progress state를 업데이트하는 함수;
=======
                console.log(response.data);
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
            } catch (error) {
                console.error('Error fetching data: ', error);
            }
        };

        fetchData();
<<<<<<< HEAD

        const intervalId = setInterval(fetchData, 5000);  // 매 5초마다 데이터를 요청합니다.
        return () => clearInterval(intervalId);  // 컴포넌트가 언마운트될 때 인터벌을 정리합니다.
    }, [authState.token, authState.username]);
    useEffect(() => {
        if (progress < targetProgress) {
            // progress가 targetProgress보다 작으면 progress를 증가시킵니다.
            const timeoutId = setTimeout(() => {
                setProgress(progress + 1);
            }, 100);  // 100ms마다 progress를 1씩 증가시킵니다.
            return () => clearTimeout(timeoutId);  // 컴포넌트 unmount 시에 timeout을 clear합니다.
        }
    }, [progress, targetProgress]); 
    if (!orderData) return <div style={{ fontSize: '40px', color: 'white' }}>주문이 없습니다.</div>; // 주문 데이터가 없는 경우
=======
    }, [authState.token, authState.username]);

    if (!orderData) return <div>주문이 없습니다.</div>; // 40폰트에 흰색으로 수정

>>>>>>> e5f4478e466ed135085eb68ad645afc355701127

    const currentTime = new Date();
    const estimatedTime = new Date(orderData.estimated_time);
    const timeDifference = estimatedTime - currentTime;
    const timeDifferenceInMinutes = Math.floor(timeDifference / 1000 / 60);

<<<<<<< HEAD
    // 상품 개수 계산
    let productCounts = {};
    if (orderData && orderData.products) {
        productCounts = orderData.products.reduce((counts, product) => {
            if (!counts[product]) {
                counts[product] = 1;
            } else {
                counts[product]++;
            }
            return counts;
        }, {});
    }
    // 상품 개수를 문자열로 변환
    //const productCountsString = Object.entries(productCounts)
    //    .map(([product, count]) => `${product}: ${count}개`)
    //    .join('\n');

    if (orderData.order_accepted === 3) {
        return <div style={{ 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center', 
            height: '100vh', 
            fontSize: '2em', 
            color: '#FF69B4',
            fontWeight: 'bold' 
        }}>
            주문 정보가 없습니다
        </div>
    }
    return (
        <div style={{ display: 'flex', flexDirection: 'row' }}>
            <div style={{ flex: 1, backgroundColor: '#FFF3FF', padding: '20px', margin: '20px', borderRadius: '10px' }}>
                <section className="bg-[#FEE2E2] py-32 md:py-6 lg:py-5">
                    <div className="container mx-auto px-0 md:px-6">
                        <div className="bg-[#FFF1F1] rounded-lg shadow-lg">
                            <div className="px-6 py-4 md:px-8 md:py-6">
                                <h2 className="text-2xl font-bold text-gray-900 mb-4">배송 정보</h2>
                            </div>
                            <div className="bg-white rounded-b-lg shadow-md px-6 py-4 md:px-8 md:py-6">
                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
                                    <div>
                                        <h3 className="text-lg font-medium text-gray-900 mb-2" style={{ marginBottom: '1px' }}>주문자</h3>
                                        <p className="text-base text-gray-700" style={{ marginBottom: '3px' }}>
                                            {orderData.customer}
                                        </p>
                                        <h2 className="text-lg font-medium text-gray-900 mb-2" style={{ marginTop: '20px', marginBottom: '1px' }}>도착지</h2>
                                        <p className="text-base text-gray-700" style={{ marginTop: '3px' }}>
                                            {orderData.destination} 지역
                                        </p>
                                    </div>
                                    <div>
                                        <h3 className="text-lg font-medium text-gray-900 mb-2">배송 상품</h3>
                                        <p className="text-base text-gray-700" style={{whiteSpace: 'pre-line'}}>
                                        <div>
                                            {orderData && orderData.products ? orderData.products.map((item, index) => (
                                                <div key={index}>
                                                    <p>{item.name} {item.quantity}개</p>
                                                </div>
                                            )) : <div style={{ fontSize: '40px', color: 'white' }}>주문이 없습니다.</div>}
                                        </div>
                                        </p>
                                    </div>
                                    <div>
                                        <h3 className="text-lg font-medium text-gray-900 mb-2">주문 코드</h3>
                                        <p className="text-base text-gray-700">{orderData.order_number}</p>
                                    </div>
                                    <div>
                                        <h3 className="text-lg font-medium text-gray-900 mb-2">도착 예상시간</h3>
                                        <p className="text-base text-gray-700">{timeDifferenceInMinutes} 분</p>
                                    </div>
                                </div>
                            </div>
                            <div className="mt-6 flex flex-col justify-center items-center" style={{ width: '100%' }}>
                                <h3 className="text-lg font-medium text-black-500 mb-2" style={{ letterSpacing: '2px', fontSize: '24px', paddingLeft: '10px' }}>진행 상황</h3>
                                <div className="relative bg-gray-200 rounded-full h-2.5 dark:bg-gray-700" style={{ width: '95%', marginLeft: '3px', marginRight: '3px' }}>
                                    <div
                                        className={progress < 50 ? "bg-red-600 h-2.5 rounded-full" : "bg-green-600 h-2.5 rounded-full"}
                                        style={{
                                            width: `${progress}%`,
                                        }}
                                    />
                                </div>
                            </div>
                            <Button
                                variant="contained" 
                                color="primary" 
                                style={{
                                    display: orderData.order_accepted !== 1 ? 'none' : 'block', // orderData.order_accepted가 1이 아닐 때 버튼 숨기기
                                    marginTop: '20px', 
                                    backgroundColor: '#FF69B4', 
                                    color: 'white', 
                                    padding: '10px 20px', 
                                    borderRadius: '5px', 
                                    fontSize: '18px', 
                                    fontWeight: 'bold'
                                }}
                                onClick={async () => {
                                    try {
                                        const username = authState.username;
                                        if (!username) return(console.error(authState.username));   

                                        const response = await axios.patch(`${config.baseURL}api/latest_order/${authState.username}/`,
                                            {
                                                order_accepted: 2
                                            },
                                            {
                                            headers: {
                                                'Authorization': `Token ${authState.token}`  // 토큰을 헤더에 추가
                                            }
                                            });
                                        console.log(response.data);
                                    } catch (error) {
                                        console.error(error);
                                    }
                                }}
                                > 배송 완료
                            </Button>
                        </div>
                    </div>
                </section>
            </div>
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', backgroundColor: '#FFF3FF', padding: '13px 13px', margin: '20px', borderRadius: '10px'}}>
                <div style={{ width: '640px', height: '320px', overflow: 'hidden', marginBottom: '20px' }}>
                    <h3 style={{ margin: '0 0 10px 0' }}>AGV 영상</h3>
                    <img
                        src={orderData?.agv?.agv_camera}
                        alt="AGV Camera"
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    />
                </div>
                <div style={{ width: '640px', height: '390px', overflow: 'hidden' }}>
                    <h3 style={{ margin: '0 0 10px 0' }}>Rack 영상</h3>
                    <img
                        src="http://172.30.1.18:7120/?action=stream"
                        alt="Rack Camera"
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    />
                </div>
            </div>
        </div>
    );
}

export default Orderwhere;
=======
        // 상품 개수 계산
    const productCounts = orderData.products.reduce((counts, product) => {
        if (!counts[product]) {
            counts[product] = 1;
        } else {
            counts[product]++;
        }
        return counts;
    }, {});

    // 상품 개수를 문자열로 변환
    const productCountsString = Object.entries(productCounts)
        .map(([product, count]) => `${product}: ${count}개`)
        .join('\n');

    return (
    <div style={{ display: 'flex', flexDirection: 'row' }}>
        <div style={{ flex: 1, backgroundColor: '#FFF3FF', padding: '20px', margin: '20px', borderRadius: '10px' }}>
            <section className="bg-[#FEE2E2] py-32 md:py-6 lg:py-5">
            <div className="container mx-auto px-0 md:px-6">
                <div className="bg-[#FFF1F1] rounded-lg shadow-lg">
                <div className="px-6 py-4 md:px-8 md:py-6">
                    <h2 className="text-2xl font-bold text-gray-900 mb-4">배송 정보</h2>
                </div>
                <div className="bg-white rounded-b-lg shadow-md px-6 py-4 md:px-8 md:py-6">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
                    <div>
                    <h3 className="text-lg font-medium text-gray-900 mb-2" style={{ marginBottom: '1px' }}>주문자</h3>
                    <p className="text-base text-gray-700" style={{ marginBottom: '3px' }}>
                        {orderData.customer}
                    </p>
                    <h2 className="text-lg font-medium text-gray-900 mb-2" style={{ marginTop: '20px', marginBottom: '1px' }}>도착지</h2>
                    <p className="text-base text-gray-700" style={{ marginTop: '3px' }}>
                        {orderData.destination} 지역
                    </p>
                    </div>
                    <div>
                        <h3 className="text-lg font-medium text-gray-900 mb-2">배송 상품</h3>
                        <p className="text-base text-gray-700"  style={{whiteSpace: 'pre-line'}}>
                        {productCountsString}
                        </p>
                    </div>
                    <div>
                        <h3 className="text-lg font-medium text-gray-900 mb-2">주문 코드</h3>
                        <p className="text-base text-gray-700">{orderData.order_number}</p>
                    </div>
                    <div>
                        <h3 className="text-lg font-medium text-gray-900 mb-2">도착 예상시간</h3>
                        <p className="text-base text-gray-700">{timeDifferenceInMinutes}</p>
                    </div>
                    </div>
                </div>

                <div className="mt-6 flex flex-col justify-center items-center" style={{ width: '100%' }}>
                    <h3 className="text-lg font-medium text-black-500 mb-2" style={{ letterSpacing: '2px', fontSize: '24px', paddingLeft: '10px' }}>진행 상황</h3>
                    <div className="relative bg-gray-200 rounded-full h-2.5 dark:bg-gray-700" style={{ width: '95%', marginLeft: '3px', marginRight: '3px' }}>
                        <div
                            className={progress < 50 ? "bg-red-600 h-2.5 rounded-full" : "bg-green-600 h-2.5 rounded-full"}
                            style={{
                                width: `${progress}%`,
                            }}
                        />
                    </div>
                </div>
            </div>
                <Button 
                    variant="contained" 
                    color="primary" 
                    style={{ 
                        marginTop: '20px', 
                        backgroundColor: '#FF69B4', 
                        color: 'white', 
                        padding: '10px 20px', 
                        borderRadius: '5px', 
                        fontSize: '18px', 
                        fontWeight: 'bold' 
                    }}> 배송 완료
                </Button>
            </div>
            </section>

        </div>
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', backgroundColor: '#FFF3FF', padding: '13px 13px', margin: '20px', borderRadius: '10px'}}>
            <div style={{ flex: 1, marginBottom: '0.25em' }}>
                <iframe title="AGV Video" src="http://172.30.1.73:8080/?action=stream" width="640" height="320" style={{ border: '2px solid black', borderRadius: '10px' }}></iframe>
            </div>
            <div style={{ flex: 1 }}>
                <iframe title="RACK Video" src="https://www.youtube.com/watch?v=gX2ZYFyGjmU" width="640" height="320" style={{ border: '2px solid black', borderRadius: '10px' }}></iframe>
            </div>
        </div>
    </div>
    );
}

export default Orderwhere;
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
