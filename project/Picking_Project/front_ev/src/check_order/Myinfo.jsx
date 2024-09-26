
import config from '../components/config.js';
import { useAuth } from '../components/AuthProvider.js';
import React, { useState, useEffect } from 'react';


function Myinfo() {
    const { authState } = useAuth();  // authState 가져오기
    const [orders, setOrders] = useState([]);
    const [userInfo, setUserInfo] = useState(null);

    useEffect(() => {
<<<<<<< HEAD
        const fetchData = () => {
            if (authState !== null && authState.username && authState.token) {
                const username = authState.username;
        
                Promise.all([
                    fetch(`${config.baseURL}accounts/my_info/${username}`, {
                        headers: {
                            'Authorization': `Token ${authState.token}`
                        }
                    }).then(response => {
                        if (!response.ok) {
                            throw new Error('API 요청 실패');
                        }
                        return response.json();
                    }).catch(error => ({error: error.message})),
                    fetch(`${config.baseURL}api/user_orders/${username}`, {
                        headers: {
                            'Authorization': `Token ${authState.token}`
                        }
                    }).then(response => {
                        if (!response.ok) {
                            throw new Error('API 요청 실패');
                        }
                        return response.json();
                    }).catch(error => ({ error: error.message }))
                ]).then(([userInfo, orders]) => {
                    if (userInfo.error) {
                        console.log(`사용자 정보 요청 오류: ${userInfo.error}`);
                    } else {
                        setUserInfo(userInfo);
                    }
                    if (orders.error) {
                        console.log(`주문 정보 요청 오류: ${orders.error}`);
                    } else {
                        setOrders(orders);
                    }
                }).catch(error => {
                    console.error('API 요청 오류:', error.message);
                });
            }
        };

        fetchData(); // 컴포넌트가 마운트될 때 한 번 호출
        const intervalId = setInterval(fetchData, 5000); // 5초마다 fetchData를 호출

        // 컴포넌트가 언마운트될 때 인터벌을 정리
        return () => clearInterval(intervalId);
=======
        if (authState !== null && authState.username && authState.token) {
            const username = authState.username;
    
            Promise.all([
                fetch(`${config.baseURL}accounts/my_info/${username}`, {
                    headers: {
                        'Authorization': `Token ${authState.token}`
                    }
                }).then(response => {
                    if (!response.ok) {
                        throw new Error('API 요청 실패');
                    }
                    return response.json();
                }).catch(error => ({error: error.message})),
                fetch(`${config.baseURL}api/user_orders/${username}`, {
                    headers: {
                        'Authorization': `Token ${authState.token}`
                    }
                }).then(response => {
                    if (!response.ok) {
                        throw new Error('API 요청 실패');
                    }
                    return response.json();
                }).catch(error => ({ error: error.message }))
            ]).then(([userInfo, orders]) => {
                if (userInfo.error) {
                    console.log(`사용자 정보 요청 오류: ${userInfo.error}`);
                } else {
                    setUserInfo(userInfo);
                }
                if (orders.error) {
                    console.log(`주문 정보 요청 오류: ${orders.error}`);
                } else {
                    setOrders(orders);
                }
            }).catch(error => {
                console.error('API 요청 오류:', error.message);
            });
        }
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
    }, [authState]);

    console.log(orders);
    console.log(userInfo);
    console.log(authState); // 디버깅

    let formattedDate = '정보 없음';
    if (userInfo && userInfo.login_time) {
        const date = new Date(userInfo.login_time);
        formattedDate = `${date.toLocaleDateString('ko-KR', { month: '2-digit', day: '2-digit' })} ${date.toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' })}`;
    }

    return (
        <section key="1" className="bg-[#FEE2E2] py-12 md:py-16 lg:py-20">
          <div className="container mx-auto px-4 md:px-6">
            <div className="bg-[#FFF1F1] rounded-lg shadow-lg">
              <div className="px-6 py-4 md:px-8 md:py-6">
                <h2 className="text-2xl font-bold text-gray-900 mb-4">My Information</h2>
              </div>
              <div className="bg-white rounded-b-lg shadow-md px-6 py-4 md:px-8 md:py-6">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:gap-6">
                  <div>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">아이디 : {userInfo && userInfo.username}</h3>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">이름 : {userInfo && userInfo.name}</h3>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">연락처 : {userInfo && userInfo.phone}</h3>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">직급 : {userInfo && userInfo.rank}</h3>
                  </div>
                  <div>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">오늘 일한 시간 : {userInfo && userInfo.day_time}</h3>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">주간 일한 시간 : {userInfo && userInfo.week_time}</h3>
                    <h3 className="text-lg font-medium text-gray-900 mb-4">마지막 로그인 시간 : {userInfo && formattedDate}</h3>
                  </div>
                </div>
                <div className="mt-6 flex justify-end">
                    <div className="relative w-full bg-gray-200 rounded-lg p-4 dark:bg-gray-700">
                        <h3 className="text-2xl font-medium text-white mb-4 flex justify-center items-center">
                            주문 목록
                            </h3>
                                <div className="bg-white p-4 rounded-lg shadow-md">
                                    <table className="min-w-full leading-normal">
                                        <thead>
                                            <tr>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    주문 번호
                                                </th>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    주문 상품
                                                </th>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    목적지
                                                </th>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    사용한 AGV
                                                </th>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    처리 결과
                                                </th>
                                                <th className="px-5 py-3 border-b-2 border-gray-200 bg-gray-800 text-left text-xs font-semibold text-white uppercase tracking-wider">
                                                    주문 날짜
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
<<<<<<< HEAD
                                        {orders.map((order, index) => (
                                            <tr key={order.id || index}>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{order.order_number}</td>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">
                                                    {order.products.map((product, productIndex) => (
                                                        <p key={productIndex}>{product.name} {product.quantity}개</p>
                                                    ))}
                                                </td>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{order.destination}</td>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{order.agv_id}</td>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{order.order_accepted === 1 ? '물건 목적지 도착' : (order.order_accepted === 0 ? '물품 배송 중' : '배송 완료')}</td>
                                                <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{order.order_time ? order.order_time : '정보 없음'}</td>
                                            </tr>
                                        ))}
=======
                                            {orders.map((orders, index) => (
                                                <tr key={orders.id || index}>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.order_number}</td>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.products}</td>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.destination}</td>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.agv_id}</td>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.order_accepted ? '배송 성공' : '배송 실패'}</td>
                                                    <td className="px-5 py-5 border-b border-gray-200 bg-white text-lg">{orders.order_time ? orders.order_time : '정보 없음'}</td>
                                                </tr>
                                            ))}
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
                                        </tbody>
                                    </table>
                        </div>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      );
  }
export default Myinfo;