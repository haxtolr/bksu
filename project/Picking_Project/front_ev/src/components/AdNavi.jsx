import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Button } from "./ui/button";
<<<<<<< HEAD
import { SheetTrigger, SheetContent, Sheet } from "./ui/sheet";
import { useAuth } from './AuthProvider.js';
import config from './config.js';
import LogoutComponent from './Logout';
import axios from 'axios';
import { ReactComponent as MountainSVG } from '/Users/heecjang/bksu/project/front_ev/src/lib/logo.svg';

=======
//import { useNavigate } from 'react-router-dom';
import { SheetTrigger, SheetContent, Sheet } from "./ui/sheet";
import { useAuth } from './AuthProvider.js';
import LogoutComponent from './Logout';
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127


export default function AdNavi() {
  const { authState, } = useAuth(); // AuthProvider에서 제공하는 상태와 함수를 가져옵니다.
  const [weeklyTime, setWeeklyTime] = useState(0);
  const [dailyTime, setDailyTime] = useState(0);

  useEffect(() => {
<<<<<<< HEAD
    const fetchTime = async () => {
      console.log('authState: ', authState);
      if (authState && authState.isLoggedIn) {
        try {
          const response = await axios.get(
            `${config.baseURL}accounts/usertime/${authState.username}`,
            {
              headers: {
                'Authorization': `Token ${authState.token}`,
              },
            }
          );
          setWeeklyTime(response.data.week_time);
          setDailyTime(response.data.day_time);
        } catch (error) {
          console.error('Error fetching time: ', error);
        }
      }
    };

    fetchTime();
  
    const weeklyTimer = setInterval(() => {
      if (authState && authState.isLoggedIn) {
        setWeeklyTime((prevTime) => prevTime + 1);
      }
    }, 60000); // 매 분마다 갱신

    // 일일 타이머 시작
    const dailyTimer = setInterval(() => {
      if (authState && authState.isLoggedIn) {
        setDailyTime((prevTime) => prevTime + 1);
      }
    }, 60000); // 매 분마다 갱신

    return () => {
=======
    let weeklyTimer, dailyTimer;
  
    // 주간 타이머 시작
    weeklyTimer = setInterval(() => {
      if (authState) { // 로그인 상태일 때
        setWeeklyTime((prevTime) => prevTime + 1);
      }
    }, 60000); // 매 분마다 갱신
  
    // 일일 타이머 시작
    dailyTimer = setInterval(() => {
      if (authState) { // 로그인 상태일 때
        setDailyTime((prevTime) => prevTime + 1);
      }
    }, 60000); // 매 분마다 갱신
  
    return () => {
      // 컴포넌트가 언마운트되면 타이머를 정리합니다.
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
      clearInterval(weeklyTimer);
      clearInterval(dailyTimer);
    };
  }, [authState]);

<<<<<<< HEAD

=======
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
  return (
    <div key="1" className="flex h-16 w-full flex-col bg-[#e0e0ff]" >
      <header className="flex h-16 w-full items-center justify-between bg-white px-4 shadow-md md:px-6" >
        <div className="flex items-center">
          <Link className="flex items-center" href="#">
            <MountainIcon className="h-6 w-6 text-[#5b5b8c]" />
            <span className="ml-2 text-xl font-bold text-[#5b5b8c]">EV</span>
          </Link>
        </div>
        <nav className="hidden items-center space-x-6 md:flex">       
          <Link
            className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
            to ="/ManageHome"
          >
            Home
          </Link>
          <Link
            className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
            to="/ManagePeople"
          >
            인사 관리 
          </Link>
          <Link
            className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
            to="/ManageProduct"
          >
            제품 관리
          </Link>
          <Link
            className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
             to ="/ManageOrder"
          >
            주문 관리
          </Link>
        </nav>
        <Sheet>
          <SheetTrigger asChild>
            <Button className="md:hidden" size="icon" variant="outline">
              <MenuIcon className="h-6 w-6 text-[#5b5b8c]" />
              <span className="sr-only">아직 테스트중</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="left">
            <div className="flex flex-col items-start space-y-6 p-6">
              <Link className="flex items-center" href="#">
                <MountainIcon className="h-6 w-6 text-[#5b5b8c]" />
                <span className="ml-2 text-xl font-bold text-[#5b5b8c]">관리자 페이지</span>
              </Link>
              <nav className="flex flex-col items-start space-y-4">
                <Link
                  className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
<<<<<<< HEAD
                  to ="/ManageHome"
=======
                  href="#"
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
                >
                  Home
                </Link>
                <Link
                  className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
                  href="#"
                >
                  Title 1
                </Link>
                <Link
                  className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
                  href="#"
                >
                  Title 2
                </Link>
                <Link
                  className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
                  href="#"
                >
                  Title 3
                </Link>
                <Link
                  className="text-[#5b5b8c] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 text-lg"
                  href="#"
                >
                  Title 4
                </Link>
              </nav>
            </div>
          </SheetContent>
        </Sheet>
        <div className="flex items-center space-x-4">
        <span className="ml-2 text-xl font-bold text-[#5b5b8c]">{authState.isLoggedIn && <span>{authState.username}</span>}  </span>
<<<<<<< HEAD
        <div className="flex items-center space-x-2">
                <ClockIcon className="h-5 w-5 text-[#5b5b8c]" />
                <span className="text-[#5b5b8c]">
                    주간: {weeklyTime !== null ? `${Math.floor(weeklyTime / 60)}시간 ${weeklyTime % 60}분` : '로딩 중...'}
                </span>
            </div>
            <div className="flex items-center space-x-2">
                <ClockIcon className="h-5 w-5 text-[#5b5b8c]" />
                <span className="text-[#5b5b8c]">
                    오늘 : {dailyTime !== null ? `${Math.floor(dailyTime / 60)}시간 ${dailyTime % 60}분` : '로딩 중...'}
                </span>
            </div>
          <LogoutComponent
            onLogout={(weeklyTime, dailyTime) => {
              clearInterval(weeklyTime);
              clearInterval(dailyTime);
            }}
            weeklyTime={weeklyTime}
            dailyTime={dailyTime}
          />
        </div>
      </header>
    </div>
  );
=======
          <div className="flex items-center space-x-2">
            <ClockIcon className="h-5 w-5 text-[#5b5b8c]" />
            <span className="text-[#5b5b8c]">주간: {weeklyTime}</span>
          </div>
          <div className="flex items-center space-x-2">
            <ClockIcon className="h-5 w-5 text-[#5b5b8c]" />
            <span className="text-[#5b5b8c]">오늘 : {dailyTime}</span>
          </div>
          <LogoutComponent />
        </div>
      </header>
    </div>
  )
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
}


function ClockIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <polyline points="12 6 12 12 16 14" />
    </svg>
  )
}


function MenuIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="4" x2="20" y1="12" y2="12" />
      <line x1="4" x2="20" y1="6" y2="6" />
      <line x1="4" x2="20" y1="18" y2="18" />
    </svg>
  )
}

<<<<<<< HEAD
function MountainIcon(props) {
  return (
    <MountainSVG
      {...props}
      width="100"
      height="100"
      viewBox="0 0 24 24" // 필요에 맞게 viewBox를 조정하세요.
      fill="currentColor"
    />  
  );
}
=======

function MountainIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  )
}
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
