import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthProvider.js';

const AuthMiddleware = ({ children }) => {
  const { authState } = useAuth();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!authState.isLoggedIn) {
      navigate('/login');
    } else {
      setLoading(false);
    }
  }, [authState, navigate]);

  if (loading) {
    return <div>Loading...</div>; // or your custom loading component
  }

  return children;
};

export default AuthMiddleware;