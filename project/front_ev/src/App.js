
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation} from 'react-router-dom';
import Home from './components/Home.jsx';
import LoginComponent from './components/Login.jsx';
import Signup from './components/Signup.jsx';
import Navi from './components/Navi.jsx';
import Myinfo from './check_order/Myinfo.jsx';
import Orderwhere from './check_order/Orderwhere.jsx';
import './styles/login.css';
import LogoutComponent from './components/Logout.jsx';
import AuthMiddleware from './components/AuthMiddleware.js';
import Check_order from './check_order/Check_order.jsx';
import ManageHome from './ad/ManageHome.jsx';
import AdNavi from './components/AdNavi.jsx';
import ManagePeople from './ad/ManagePeople.jsx';
import ManageProduct from './ad/ManageProduct.jsx';
import ManageOrder from './ad/ManageOrder.jsx';


function Footer() {
  const [time, setTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => {
      clearInterval(timer);
    };
  }, []);

  return (
     <div className="bg-[#5C3C92] text-white p-4 text-center">
   <p className="mb-2">현재 시간: {time.toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' })}</p>
   <p>연락처: 010-1234-5678</p>
  </div>
  );
}


function Main() {
  const location = useLocation();
  const [cart, setCart] = useState([]);

  const addToCart = (item) => {
    if (cart.length >= 5) {
      alert('더 이상 추가할 수 없습니다');
    } else {
      setCart([...cart, item]);
    }
  };
  
  const removeFromCart = (index) => {
    setCart(cart.filter((_, i) => i !== index));
  };
  
  return (
    <>
       {['/ManageHome', '/ManagePeople', '/ManageOrder', '/ManageProduct'].includes(location.pathname) ? <AdNavi /> :
        ['/login', '/signup'].includes(location.pathname) ? null : <Navi />}
      <Routes>
        <Route path="/signup" element={<Signup/>} />
        <Route path="/login" element={<LoginComponent/>} />
        <Route path="/logout" element={<LogoutComponent/>} />
        <Route path="/home" element={
          <AuthMiddleware>
           <Home cart={cart} addToCart={addToCart} removeFromCart={removeFromCart} />
          </AuthMiddleware>
        } />
        <Route path="/Check_order" element={
         <AuthMiddleware>
          <Check_order cart={cart} addToCart={addToCart} removeFromCart={removeFromCart} />
         </AuthMiddleware>
        } />
        <Route path="/orderwhere" element={
          <AuthMiddleware>
          <Orderwhere cart={cart} addToCart={addToCart} removeFromCart={removeFromCart} />
         </AuthMiddleware>
        } />
        <Route path="/myinfo" element={
          <AuthMiddleware>
          <Myinfo cart={cart} addToCart={addToCart} removeFromCart={removeFromCart} />
         </AuthMiddleware>
        } />
        <Route path="/ManageHome" element={
          <AuthMiddleware>
           <ManageHome />
          </AuthMiddleware>
        } />  

        <Route path="/ManagePeople" element={
          <AuthMiddleware>
           <ManagePeople />
          </AuthMiddleware>
        } />  

        <Route path="/ManageProduct" element={
          <AuthMiddleware>
           <ManageProduct />
          </AuthMiddleware>
        } />  

         <Route path="/ManageOrder" element={
          <AuthMiddleware>
           <ManageOrder />
          </AuthMiddleware>
        } />  
        
  </Routes>
  <div className="bg-[#e0e0ff] dark:bg-[#e0e0ff]">
  <Footer />
  </div>
    </>
  );
}

function App() {
  return (
    <Router>
     <div className="bg-[#e0e0ff] dark:bg-[#e0e0ff]">
      <Main />
     </div>
    </Router>
  );
}

export default App;
