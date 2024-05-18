
import config from './config';
import axios from 'axios';
import '../styles/login.css';
import { Label } from "./ui/label"
import { Input } from "./ui/input"
import { Button } from "./ui/button"
import { useState } from "react";
import React from "react"
import { useNavigate } from "react-router-dom";
import { Link } from 'react-router-dom';
import { useAuth } from './AuthProvider';

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

export default function LoginComponent() {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();
  const { setAuthState } = useAuth();
  axios.defaults.baseURL = config.baseURL;;

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios({
        method: 'post',
        url: '/accounts/login/',
        data: {
          username: username,
          password: password
        },
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        withCredentials: true
      });
      if (response.data.message === 'Login successful.') {
        console.log('Login successful');
        setAuthState({ username: username, 
                      isLoggedIn: true, 
                      token: response.data.user.token, 
                      is_staff: response.data.user.is_staff 
        }); // 로그인 상태 업데이트
        if(response.data.user.is_staff == true)
          navigate('/ManageHome');  // 관리자 화면으로 이동
        else        
          navigate('/home');  // 홈 화면으로 이동
      } 
      else if (response.data.auth_error && response.data.auth_error[0]  === 'id pw error') {
        console.error('Login failed');
        setErrorMessage('틀린 아이디와 비밀번호입니다. 다시 시도해주세요.');
      }
      else if (response.data.auth_error && response.data.auth_error[0] === 'pending approval') {
        console.error('approval pending');
        setErrorMessage('비활성화된 계정입니다. 관리자에게 문의하세요.');
      }
      else if (response.data.auth_error && response.data.auth_error[0] === 'using') 
      {
        console.error('already logged in');
        setErrorMessage('이미 로그인 중입니다.');
      }
      else {
        console.error('Server error. Please try again.');
        setErrorMessage('서버 오류입니다. 다시 시도해주세요.');
      }
      console.log(response.data.message);
    }
    catch (error) {
      console.log(error);
      setErrorMessage('서버 오류 입니다.'); // 서버 오류
    }
  };
  
  return (
    <div className="flex h-screen w-full items-center justify-center bg-[#e0e0ff] ">
      <div className="mx-4 w-full max-w-md space-y-6 rounded-lg bg-white p-6 shadow-lg ">
        <form onSubmit={handleSubmit}>
        <div className="flex items-center justify-center">
          <h1 className="text-3xl font-bold text-[#5b5b8c] ">EV</h1>
        </div>
        <div className="space-y-4">
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="username">
              아이디
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none "
              id="username"
              placeholder="아이디를 입력해주세요."
              type="text"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
            />
          </div>
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="password">
              비밀번호
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none "
              id="password"
              placeholder="비밀번호를 입력해주세요"
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
          </div>
          <div className="space-y-2">
            <Button
              className="w-full rounded-md bg-[#9090c0] py-2 font-medium text-white hover:bg-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2"
              type="submit"
            >
              로그인
            </Button>
          </div>
        </div>
          </form>
          <div>
            <div className="flex items-center justify-between">
              <Link
                className="text-[#9090c0] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2"
                variant="link"
                as = {Link}
                to = "/signup"
              >
                회원가입
              </Link>
            </div>
          </div>
          {errorMessage && (
          <div className="rounded-md bg-[#e0e0ff] p-4 text-[#5b5b8c]">
            <p>{errorMessage}</p>
          </div>
          )}
          {/*<div className="rounded-md bg-[#e0e0ff] p-4 text-[#5b5b8c] dark:bg-[#3c3c4f] dark:text-white">
            <p>Incorrect username or password</p>
          </div>*/}
        </div>
      </div>
  );
}
