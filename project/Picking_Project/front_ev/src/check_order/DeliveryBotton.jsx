import React, { useState } from 'react';
import DeliveryStatus from './DeliveryStatus';
import { useAuth } from '../components/AuthProvider.js'; // useAuth 훅을 가져옵니다.
import config from '../components/config.js';

function DeliveryButton({ cart, deliveryLocation }) {
    const [message, setMessage] = useState('');
    const { status } = DeliveryStatus({ cart });
    const { authState } = useAuth();

    const handleDelivery = async () => {
        if (!status) {
            console.log(status);
            setMessage('배송이 불가능합니다.');
            return;
        }

        const deliveryData = {
            customer: authState.username, // 작성자 아이디를 여기에 입력하세요.
            destination: deliveryLocation, // 배송받을 위치를 여기에 입력하세요.
            products: cart.map(item => item.id ), // 카트에 담긴 각 항목의 id를 객체 형태로 배열로 만듭니다.
        };
        
        console.log(JSON.stringify(deliveryData, null, 2)); // deliveryData 객체를 JSON 형식으로 출력합니다.
        
        const response = await fetch(`${config.baseURL}api/orders/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Token ${authState.token}`,
            },
            body: JSON.stringify(deliveryData),
        });
    
        if (response.ok) {
<<<<<<< HEAD
            setMessage({ type: 'success', text: '배송 요청을 성공하셨습니다.'});
        } else {
            setMessage({ type : 'error', text :'배송 요청이 실패했습니다. 배송 위치, 상품 수량을 확인해주세요.'});
        }
    };
    
=======
            setMessage('배송 성공하셨습니다.');
        } else {
            setMessage('배송 요청이 실패했습니다.');
        }
    };

>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
    return (
        <div>
            <button 
                onClick={handleDelivery} 
                style={{
                    backgroundColor: '#87CEEB', /* Green */
                    border: 'none',
                    color: 'white',
                    padding: '15px 32px',
                    textAlign: 'center',
                    textDecoration: 'none',
                    display: 'inline-block',
                    fontSize: '16px',
                    margin: '4px 2px',
                    cursor: 'pointer',
                    borderRadius: '12px',
                    transitionDuration: '0.4s',
                }}
                onMouseOver={e => e.target.style.backgroundColor = "#7EC0EE"}
                onMouseOut={e => e.target.style.backgroundColor = "#87CEEB"}
            >
                배송
            </button>
<<<<<<< HEAD
            {message.text && <p style={{ color: message.type === 'error' ? 'red' : 'green' }}>{message.text}</p>}
=======
            {message && <p>{message}</p>}
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
        </div>
    );
}

export default DeliveryButton;