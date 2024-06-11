// LogoutComponent.jsx

import React, { useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthProvider.js";
import config from "./config.js";
import { Button } from "./ui/button.jsx";

const LogoutComponent = ({ onLogout, weeklyTime, dailyTime }) => {
  const navigate = useNavigate();
  const { authState, setAuthState } = useAuth();

  useEffect(() => {
    // 컴포넌트가 마운트되었을 때 타이머 중지 함수 호출
    return () => {
      onLogout(weeklyTime, dailyTime);
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const handleLogout = async () => {
    if (authState.isLoggedIn) {
      try {
        // weeklyTime, dailyTime 값을 서버에 전송
        await axios.post(
          `${config.baseURL}accounts/logout/`,
          {
            week_time: weeklyTime,
            day_time: dailyTime
          },
          {
            withCredentials: true,
            headers: {
              Authorization: `Token ${authState.token}`,
            },
          }
        );

        setAuthState({ username: "", isLoggedIn: false, token: "" });
        navigate("/login");
        console.log(weeklyTime, dailyTime);
      } catch (error) {
        console.error("로그아웃 에러:", error);
      }
    } else {
      console.error("Login failed");
    }
  };

  return (
    <Button
      className="rounded-md bg-[#9090c0] py-2 px-4 font-medium text-white hover:bg-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 dark:bg-[#707090] dark:hover:bg-[#606080] dark:focus:ring-[#707090]"
      variant="solid"
      onClick={handleLogout}
    >
      Logout
    </Button>
  );
};

export default LogoutComponent;
