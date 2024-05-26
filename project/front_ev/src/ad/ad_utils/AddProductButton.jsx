import React, { useState } from 'react';
import { Button, Modal, Box, Typography, TextField } from '@mui/material';
import axios from 'axios';
import { useAuth } from '../../components/AuthProvider.js';
import config from '../../components/config.js';

const AddProductButton = () => {
  const { authState } = useAuth();
  const [open, setOpen] = useState(false);
  const [productName, setProductName] = useState('');
  const [preview1, setPreview1] = useState('');
  const [quantity, setQuantity] = useState('');
  const [locationX, setLocationX] = useState('');
  const [locationY, setLocationY] = useState('');
  const [volume, setVolume] = useState('');
  const [standard, setStandard] = useState('');
  const [specialStandard, setSpecialStandard] = useState('');
  const [precision, setPrecision] = useState('');
  const [productImage, setProductImage] = useState(null);
  const [detailImage, setDetailImage] = useState(null);
  const [error, setError] = useState('');

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const handleSubmit = async () => {
    // 유효성 검사
    if (!productName || !preview1 || !quantity || !locationX || !locationY || !productImage) {
      setError('모든 필드를 입력해주세요.');
      return;
    }

    if (isNaN(quantity) || quantity <= 0) {
      setError('수량은 유효한 숫자여야 합니다.');
      return;
    }

    if (isNaN(locationX) || isNaN(locationY)) {
      setError('위치 번호는 숫자여야 합니다.');
      return;
    }

    const formData = new FormData();
    formData.append('product_name', productName);
    formData.append('preview1', preview1);
    formData.append('quantity', quantity);
    formData.append('location_number', `${locationX} - ${locationY}`);
    formData.append('product_image', productImage);
    formData.append('detail_image', detailImage);
    formData.append('volume', volume);
    formData.append('standard', standard);
    formData.append('special_standard', specialStandard);
    formData.append('precision', precision);

    try {
      const response = await axios.post(`${config.baseURL}products/products/`, formData, {
        headers: {
          'Authorization': `Token ${authState.token}`,
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('Product added successfully:', response.data);
      handleClose();
    } catch (error) {
      console.error('Error adding product:', error);
      setError('제품 추가 중 오류가 발생했습니다.');
    }
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    const name = e.target.name;
    if (name === 'product_image') {
      setProductImage(file);
    } else if (name === 'detail_image') {
      setDetailImage(file);
    }
  };

  return (
    <div>
      <Button variant="contained" onClick={handleOpen}>
        상품 추가
      </Button>
      <Modal open={open} onClose={handleClose}>
        <Box sx={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', width: 400, bgcolor: 'background.paper', border: '2px solid #000', boxShadow: 24, p: 4 }}>
          <Typography variant="h6" component="h2">
            상품 추가
          </Typography>
          <TextField fullWidth label="제품명" value={productName} onChange={(e) => setProductName(e.target.value)} sx={{ my: 2 }} />
          <TextField fullWidth label="제품 정보" value={preview1} onChange={(e) => setPreview1(e.target.value)} sx={{ my: 2 }} />
          <TextField fullWidth label="수량" type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} sx={{ my: 2 }} />
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
            <span style={{ whiteSpace: 'nowrap' }}>상품 사진 :</span>
            <input type="file" name="product_image" accept="image/*" onChange={handleImageChange} />
            </div>
            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>  
            <span style={{ whiteSpace: 'nowrap' }}>디테일 사진 :</span>
            <input type="file" name="detail_image" accept="image/*" onChange={handleImageChange} />
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <TextField label="위치 X" type="number" value={locationX} onChange={(e) => setLocationX(e.target.value)} />
            <TextField label="위치 Y" type="number" value={locationY} onChange={(e) => setLocationY(e.target.value)} />
          </div>
          <TextField fullWidth label="용량" value={volume} onChange={(e) => setVolume(e.target.value)} sx={{ my: 2 }} />
          <TextField fullWidth label="표준" value={standard} onChange={(e) => setStandard(e.target.value)} sx={{ my: 2 }} />
          <TextField fullWidth label="특수 표준" value={specialStandard} onChange={(e) => setSpecialStandard(e.target.value)} sx={{ my: 2 }} />
          <TextField fullWidth label="정밀도" value={precision} onChange={(e) => setPrecision(e.target.value)} sx={{ my: 2 }} />
          <Button variant="contained" onClick={handleSubmit}>
            확인
          </Button>
          {error && <Typography color="error">{error}</Typography>}
        </Box>
      </Modal>
    </div>
  );
};

export default AddProductButton;
