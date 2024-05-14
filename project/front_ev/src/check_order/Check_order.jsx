import React, { useState } from 'react';
import { Card, CardContent, Typography, Button } from '@material-ui/core';
import { Label } from "../components/ui/label"
import Select from 'react-select';
import DeleteIcon from '@mui/icons-material/Delete';

function Check_order({ cart, removeFromCart }) {
  const [location, setLocation] = useState('');

  const homeStyle = {
    backgroundColor: '#D8BFD8',
    color: '#1c2630',
    borderRadius: '10px',
    padding: '10px'
  };


  const options = [
    { value: 'a', label: 'a' },
    { value: 'b', label: 'b' },
    { value: 'c', label: 'c' },
    { value: 'd', label: 'd' },
  ];

  const styles = {
    option: (provided, state) => ({
      ...provided,
      fontWeight: state.isSelected ? 'bold' : 'normal',
      color: 'black',
      backgroundColor: state.data.color,
      fontSize: state.isFocused ? '20px' : '16px',
    }),
    singleValue: (provided, state) => ({
      ...provided,
      color: state.data.color,
      fontSize: state.selectProps.myFontSize
    })
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
      <div style={{ width: '48%' }}>
      <h3 style={{ 
        textAlign: 'center', // 텍스트를 가운데로 정렬
        fontWeight: 'bold', // 글자를 굵게
        backgroundColor: '#D8BFD8', // 배경색을 파스텔톤 보라     색으로
        color: '#1c2630', // 글자색을 하얀색으로
        borderRadius: '10px', // 모서리를 둥글게 깍음
        padding: '10px' // 내부 패딩 추가
                }}>
        주문 목록 </h3>
        {cart.map((item, index) => (
           <Card key={index} style={{ margin: '10px' }}>
           <CardContent>
             <Typography variant="h5" component="div">
               {item.product_name}
             </Typography>
             <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Typography variant="body1" color="text.secondary">
                    {item.preview1}
                  </Typography>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Typography variant="body2" color="text.secondary">
                    {item.location_number}
                  </Typography>
                    <DeleteIcon onClick={() => removeFromCart(index)} />
              </div>
           </CardContent>
          </Card>
        ))}
      </div>
      <div style={{ width: '50%', ...homeStyle }}>
      <h4 style={{ 
        textAlign: 'center', // 텍스트를 가운데로 정렬
        fontWeight: 'bold', // 글자를 굵게
        backgroundColor: '#800080', // 배경색을 파스텔톤 보라색으로
        color: 'white', // 글자색을 하얀색으로
        borderRadius: '10px', // 모서리를 둥글게 깍음
        padding: '10px' // 내부 패딩 추가
                }}>
        배송 준비</h4>
        <div style={{ backgroundColor: '#f8f8f8', padding: '20px', borderRadius: '10px', margin: '10px 0' }}>
          <p style={{ fontSize: '40px', margin: '10px 0' }}>배송 가능 여부</p>
          <div style={{ height: '40px', width: '99%', backgroundColor: 'green', margin: '10px', borderRadius: '15px' }}></div>
        </div>
        <div style={{ backgroundColor: '#f8f8f8', padding: '20px', borderRadius: '10px', margin: '10px 0' }}>
           <label htmlFor="location" style={{ fontSize: '40px', margin: '30px 30px' }}>배송 받을 위치</label>
              <Select
                myFontSize="20px"
                options={options}
                styles={styles}
                onChange={(e) => setLocation(e.value)}
              />
        </div>
        <Button variant="contained" color="primary" style={{ marginTop: '20px', fontSize: '20px', padding: '15px 30px' }}>
          배송 
        </Button>
      </div>
    </div>
  );
}

export default Check_order;