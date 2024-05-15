import { Card, CardContent, CardMedia, Typography, Grid, Button } from '@mui/material';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import DeleteIcon from '@mui/icons-material/Delete';
import { useState, useEffect } from 'react';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';
import NavigateNextIcon from '@mui/icons-material/NavigateNext';
import config from './config.js';
import { Link } from 'react-router-dom';
import { useAuth } from '../components/AuthProvider.js';

import '../styles/media.css';

const Home = ({ cart, addToCart, removeFromCart }) => {

  const [products, setProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [page, setPage] = useState(1);
  const { authState } = useAuth();

  const fetchData = async () => {
    try {
      const response = await fetch(`${config.baseURL}products/getpro/`, {
        headers: {
          'Authorization': `Token ${authState.token}`
        },
      });
      const data = await response.json();
      if (!Array.isArray(data)) {
        console.error('Data is not an array');
        setProducts([]); // 데이터가 배열이 아닐 경우 빈 배열을 설정
      } else {
        setProducts(data); // 상품 데이터를 상태로 설정
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  // 컴포넌트가 마운트되면 데이터를 가져오기
  useEffect(() => {
    fetchData();
  }, []);

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const getPageNumber = (description) => {
    if (!description) {
      return null; // description이 없는 경우 null 반환
    }
    const match = description.match(/(\d+) - \d+/);
    const pageNumber = match ? Number(match[1]) : null;
    console.log(`description: ${description}, pageNumber: ${pageNumber}`);
    return pageNumber;
  };
  

  const handlePrevPage = () => {
   setPage(prevPage => prevPage > 1 ? prevPage - 1 : 4);
  };

  const handleNextPage = () => {
    setPage(prevPage => prevPage < 4 ? prevPage + 1 : 1);
  };


  return (
    <div className='layout' style={{ display: 'flex', flexDirection: 'column' }}>
      <div className='pagination' style={{ textAlign: 'center', color: '#ffffff', marginLeft: '304px' }}>
        <button onClick={handlePrevPage}><NavigateBeforeIcon /></button>
        <span style={{ fontSize: '2em', margin: '0 20px' }}>{page}번 렉 </span>
        <button onClick={handleNextPage}><NavigateNextIcon /></button>
      </div>
      <div className='home' style={{ display: 'flex', flexDirection: 'row' }}>
      <div className='cart' style={{ flex: '1', overflowY: 'auto', maxHeight: '100vh', backgroundColor: '#9090c0', 
      borderRadius: '10px', // 모서리를 둥글게 깍음
      padding: '10px',
      margin: '8px',
      marginTop: '8px',
      marginBottom: '8px'
      }}>
        <input
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={handleSearchChange}
        style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
      />
    <div>
    </div>
      <h3 style={{ 
        textAlign: 'center', // 텍스트를 가운데로 정렬
        fontWeight: 'bold', // 글자를 굵게
        backgroundColor: '#D8BFD8', // 배경색을 파스텔톤 보라색으로
        color: '#1c2630', // 글자색을 하얀색으로
        borderRadius: '10px', // 모서리를 둥글게 깍음
        padding: '10px' // 내부 패딩 추가
                }}>
        장바구니 목록 </h3>
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
       <Link
       className="text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:ring-offset-2 text-lg"
       to="/check_order"
       style={{ padding: '10px 20px', borderRadius: '4px', textDecoration: 'none' }}
     >
       주문 확인
     </Link>
      </div>
      <Grid className='grid' container spacing={0.5} style={{ flex: '4', padding: '8px', margin: '-4px' }}>
          {products
            .filter(item => {
              if (searchTerm) {
                return item.title ? item.title.includes(searchTerm) : false;
              } else {
                return getPageNumber(item.location_number) === page;
              }
            })
            .map((item, index) => (
              <Grid item xs={4} key={index}>
                <Card className='card' style={{ width: '90%', height: '100%', margin: '4px' }}>
                  <CardMedia
                    component="img"
                    height="100"
                    image={item.product_image}
                    alt="item image"
                  />
              <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                  {item.product_name}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {item.preview1}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {item.quantity}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  위치 : {item.location_number}
                </Typography>
                <Button
                  variant="contained"
                  color="primary"
                  startIcon={<AddShoppingCartIcon />}
                  onClick={() => addToCart(item)}
                >
                  장바구니 추가
                </Button>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </div>
    </div>
  );
};

export default Home;