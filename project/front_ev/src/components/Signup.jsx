/**
 * v0 by Vercel.
 * @see https://v0.dev/t/9on9EaGgS5t
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import config from './config';
import '../styles/login.css';
import { Label } from "./ui/label"
import { Input } from "./ui/input"
import { Button } from "./ui/button"
import { useState } from "react";
import React from "react"
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { Link } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

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

export default function Component() {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [, setPasswordError] = useState(true);
  const [confirmpassword, setConfirmPassword] = React.useState("");
  const [phone, setPhone] = React.useState("");
  const [name, setName] = React.useState("");
  const [, setErrorMessage] = useState("");
  const navigate = useNavigate();
  axios.defaults.baseURL = config.baseURL;
  const [usernameExists, setUsernameExists] = useState(false);
  const checkUsernameExists = async (username) => {
    try {
        const response = await axios.get(`/accounts/signup/${username}`);
        setUsernameExists(response.data.exists);
    } catch (error) {
        console.error(error);
    }
    };
  //const [, setMessage] = useState('');
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios({
        method: 'post',
        url: '/accounts/signup/',
        data: {
          username: username,
          password: password,
          phone: phone,
          name: name
        },
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        withCredentials: true
      });
        if (response.data.message === 'Signup successful.') {
            console.log('Signup successful');
            toast.success('회원가입이 완료되었습니다. 승인을 대기 중입니다.');
            setTimeout(() => {
              navigate('/login');
            }, 3000);
        } 
        else if (response.data.auth_error && response.data.auth_error[0]  === 'id error') {
            console.error('Signup failed');
            toast.error('이미 존재하는 아이디 입니다.');
            setErrorMessage('이미 존재하는 아이디 입니다.');
        }
    }
    catch (error) {
      console.log(error);
      setErrorMessage('서버 오류 입니다.'); // 서버 오류
    }
  };

  return (
    <>
    <ToastContainer />
    <div className="flex h-screen w-full items-center justify-center bg-[#e0e0ff]">
      <div className="mx-4 w-full max-w-md space-y-6 rounded-lg bg-white p-6 shadow-lg ">
        <div className="flex items-center justify-center">
          <h1 className="text-3xl font-bold text-[#5b5b8c] ">회원가입</h1>
        </div>
        <div className="space-y-4">
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="username">
              아이디
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none"
              id="username"
              placeholder="아이디를 입력하세요"
              required
              type="text"
              value={username}
              onChange={async (event) => {
                setUsername(event.target.value)
                await checkUsernameExists(event.target.value);
            }}
            />
            {!username && <p className="mt-1 text-sm text-red-500">아이디를 입력해주세요.</p>}
            {usernameExists && <p className="mt-1 text-sm text-red-500">이미 존재하는 아이디입니다.</p>}
          </div>
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="password">
              비밀번호
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none"
              id="password"
              placeholder="비밀번호를 입력하세요"
              required
              minLength="8"
              type="password"
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
                setPasswordError(event.target.value.length < 8);
              }}
            />
            {!password && <p className="mt-1 text-sm text-red-500">비밀번호를 입력해주세요.</p>}
            {(password.length < 8) && <p className="mt-1 text-sm text-red-500">비밀번호는 8자 이상이어야 합니다.</p>}
          </div>
          <div>
            <Label className="text-[#5b5b8c] " htmlFor="password-confirm">
              비밀번호 확인
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none "
              id="password-confirm"
              placeholder="비밀번호를 다시 입력하세요"
              required
              type="password"
              value={confirmpassword}
              onChange={(event) => setConfirmPassword(event.target.value)}
            />
            {!(confirmpassword === password) && <p className="mt-1 text-sm text-red-500">비밀번호가 일치하지 않습니다.</p>}
          </div>
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="name">
              이름
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none "
              id="name"
              placeholder="이름을 입력하세요"
              required
              type="text"
              value={name}
              onChange={(event) => setName(event.target.value)}
            />
            {!name && <p className="mt-1 text-sm text-red-500">이름을 입력해주세요.</p>}
          </div>
          <div>
            <Label className="text-[#5b5b8c]" htmlFor="phone">
              전화번호
            </Label>
            <Input
              className="mt-1 w-full rounded-md border border-[#d0d0e0] bg-[#f8f8f8] px-3 py-2 text-[#5b5b8c] placeholder:text-[#a0a0b0] focus:border-[#9090c0] focus:outline-none "
              id="phone"
              placeholder="전화번호를 입력하세요"
              required
              type="tel"
              value={phone}
              onChange={(event) => setPhone(event.target.value)}
            />
            {!name && <p className="mt-1 text-sm text-red-500">전화번호를 입력해주세요.</p>}
          </div>
          <div className="space-y-2">
            <Button
              className="w-full rounded-md bg-[#9090c0] py-2 font-medium text-white hover:bg-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2"
              type="submit"
              disabled={!(username && password && confirmpassword && phone && name && (password === confirmpassword))}
              onClick={handleSubmit}
              onTouchStart={handleSubmit}
            >
              회원가입
            </Button>
            <div className="flex items-center justify-between">
              <Link
                className="text-[#9090c0] hover:text-[#7070b0] focus:outline-none focus:ring-2 focus:ring-[#9090c0] focus:ring-offset-2"
                variant="link"
                as = {Link}
                to = "/login"
              >
                로그인
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </>
  );
}