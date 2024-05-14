import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import { useAuth } from './AuthProvider.js';
import config from './config.js';
import { Button } from "./ui/button.jsx";

const LogoutComponent = () => {
  const navigate = useNavigate();
  
  const { authState, setAuthState } = useAuth();
  const [, setErrorMessage] = useState('');

  axios.defaults.baseURL = config.baseURL;;

  const handleLogout = async () => {
  console.log(authState);

    if (authState.isLoggedIn) {
    try {
      await axios.post('/accounts/logout/', null, {
        withCredentials: true,
        headers: {
          Authorization: `Token ${authState.token}`
        }
      });
      setAuthState({ username: "", isLoggedIn: false, token: "" }); // 로그아웃 상태 업데이트
      navigate('/login');  // 로그인 화면으로 이동
    } catch (error) {
      console.error('로그아웃 에러:', error);
    }
  }else {
    console.error('Login failed');
    setErrorMessage('이미 로그인 중입니다.');
  }
  };

  return (
  <Button
            className="rounded-md bg-[#9090c0] py-2 px-4 font-medium text-white hover:bg-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2 dark:bg-[#707090] dark:hover:bg-[#606080] dark:focus:ring-[#707090]"
            variant="solid"
            onClick={handleLogout}
          >
            Logout
          </Button>);

}

export default LogoutComponent;