<<<<<<< HEAD
// ManaedProduct.jsx
import React, { useState, useEffect } from 'react';
import {
  Button,
  Collapse,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Card,
  CardHeader,
  CardContent,
  Typography,
  IconButton,
  Box,
  TableSortLabel,
  Modal,
  TextField,
} from '@mui/material';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import { ExpandMore } from '@mui/icons-material';
import { ResponsiveLine } from '@nivo/line';
import { ResponsiveBar } from '@nivo/bar';
import { ResponsivePie } from '@nivo/pie';
import config from '../components/config.js';
import { useAuth } from '../components/AuthProvider.js';
import AddProductButton from './ad_utils/AddProductButton.jsx';
import ProductPie from './ad_utils/productPie.jsx';
import InventoryChart from './ad_utils/ProductBar.jsx';


function ManageProduct({ authToken }) {
  const { authState } = useAuth();
  const [open, setOpen] = useState(false);
  const [products, setProducts] = useState([]);
  const [order, setOrder] = useState('asc');
  const [orderBy, setOrderBy] = useState('product_name');
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [imageModalOpen, setImageModalOpen] = useState(false);
  const [detailModalOpen, setDetailModalOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  // 검색어를 업데이트
  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };
  
  // 제품을 필터링
  const filteredProducts = products.filter((product) =>
    product.product_name.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  const handleToggle = () => {
    setOpen(!open);
  };

  const fetchProducts = () => {
    fetch(`${config.baseURL}products/`, {
      headers: {
        'Authorization': `Token ${authState.token}`
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log(data); 
        if (data.products) {
          return fetch(data.products, {
            headers: {
              'Authorization': `Token ${authState.token}`
            }
          });
        } else {
          throw new Error('Products endpoint not found');
        }
      })
      .then(response => response.json())
      .then(products => {
        console.log(products);
        if (Array.isArray(products)) {
          setProducts(products);
        } else {
          console.error('Products data is not an array:', products);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  useEffect(() => {
    fetchProducts();
    const intervalId = setInterval(fetchProducts, 3000); // fetch data every 5 seconds

    return () => clearInterval(intervalId); // clean up interval on component unmount
  }, [authState.token]);


  const handleRequestSort = (property) => {
    const isAsc = orderBy === property && order === 'asc';
    setOrder(isAsc ? 'desc' : 'asc');
    setOrderBy(property);
  };

  const sortedProducts = products.sort((a, b) => {
    if (a[orderBy] < b[orderBy]) {
      return order === 'asc' ? -1 : 1;
    }
    if (a[orderBy] > b[orderBy]) {
      return order === 'asc' ? 1 : -1;
    }
    return 0;
  });

  const handleImageClick = (product) => {
    setSelectedProduct(product);
    setImageModalOpen(true);
  };

  const handleDetailClick = (product) => {
    setSelectedProduct(product);
    setDetailModalOpen(true);
  };

  const handleCloseModal = () => {
    setImageModalOpen(false);
    setDetailModalOpen(false);
    setSelectedProduct(null);
  };

  return (
    <Box sx={{ maxWidth: '1200px', mx: 'auto', py: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4" component="h1" fontWeight="bold">
         제품 관리
        </Typography>
         <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
           <TextField
              label="제품 검색"
              variant="outlined"
              value={searchTerm}
              onChange={handleSearchChange}
              fullWidth
            />
      <AddProductButton />
      </Box>
    </Box>
    <Card>
        <CardHeader
          title="All Products"
          action={
            <IconButton onClick={handleToggle}>
              <ExpandMore />
            </IconButton>
          }
          sx={{ bgcolor: 'background.default' }}
        />
        <Collapse in={open}>
          <CardContent>
            <Table>
              <TableHead className="bg-gray-200">
                <TableRow>
                  <TableCell>
                    <TableSortLabel
                      active={orderBy === 'product_name'}
                      direction={orderBy === 'product_name' ? order : 'asc'}
                      onClick={() => handleRequestSort('product_name')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      제품명
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderBy === 'preview1'}
                      direction={orderBy === 'preview1' ? order : 'asc'}
                      onClick={() => handleRequestSort('preview1')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      제품정보
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderBy === 'quantity'}
                      direction={orderBy === 'quantity' ? order : 'asc'}
                      onClick={() => handleRequestSort('quantity')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      수량
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderBy === 'location_number'}
                      direction={orderBy === 'location_number' ? order : 'asc'}
                      onClick={() => handleRequestSort('location_number')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      위치
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderBy === 'date_received'}
                      direction={orderBy === 'date_received' ? order : 'asc'}
                      onClick={() => handleRequestSort('date_received')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      입고일
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>사진</TableCell>
                  <TableCell>상세 정보</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {filteredProducts.map((product) => (
                  <TableRow key={product.id}>
                    <TableCell>{product.product_name}</TableCell>
                    <TableCell>{product.preview1}</TableCell>
                    <TableCell>{product.quantity}</TableCell>
                    <TableCell>{product.location_number}</TableCell>
                    <TableCell>{product.date_received}</TableCell>
                    <TableCell>
                      <Button onClick={() => handleImageClick(product)}>사진 보기</Button>
                    </TableCell>
                    <TableCell>
                      <Button onClick={() => handleDetailClick(product)}>상세 정보</Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Collapse>
      </Card>
      <Box sx={{ 
  display: 'grid', 
  gap: 2, 
  mt: 3, 
  gridTemplateColumns: '1fr 1fr', // 각 열이 동일한 비율로 나누어집니다.
  height: '500px', // 박스의 높이를 500px로 설정합니다.
}}>
  <Card>
    <CardHeader title="재고 차트"/>
    <CardContent>
      <InventoryChart products={filteredProducts} />
    </CardContent>
  </Card>
  <Card>
    <CardHeader title="주문이 많이 된 지역" />
    <CardContent>
      <ProductPie />
    </CardContent>
  </Card>
</Box>
      <Modal open={imageModalOpen} onClose={handleCloseModal}>
        <Box sx={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', width: 400, bgcolor: 'background.paper', border: '2px solid #000', boxShadow: 24, p: 4 }}>
          <Typography variant="h6" component="h2">
            제품 이미지
          </Typography>
          {selectedProduct && <img src={selectedProduct.product_image} alt={selectedProduct.product_name} style={{ width: '100%' }} />}
        </Box>
      </Modal>
      <Modal open={detailModalOpen} onClose={handleCloseModal}>
        <Box sx={{ position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', width: 600, bgcolor: 'background.paper', border: '2px solid #000', boxShadow: 24, p: 4 }}>
          <Typography variant="h6" component="h2">
            제품 상세 정보
          </Typography>
          {selectedProduct && (
            <Box>
              <img src={selectedProduct.product_image} alt={selectedProduct.product_name} style={{ width: '100%' }} />
              <Typography variant="body1"><strong>제품명:</strong> {selectedProduct.product_name}</Typography>
              <Typography variant="body1"><strong>제품정보:</strong> {selectedProduct.preview1}</Typography>
              <Typography variant="body1"><strong>수량:</strong> {selectedProduct.quantity}</Typography>
              <Typography variant="body1"><strong>위치:</strong> {selectedProduct.location_number}</Typography>
              <Typography variant="body1"><strong>용량:</strong> {selectedProduct.volume}</Typography>
              <Typography variant="body1"><strong>규격:</strong> {selectedProduct.standard}</Typography>
              <Typography variant="body1"><strong>정밀도:</strong> {selectedProduct.precision}</Typography>
              <Typography variant="body1"><strong>특수 규격:</strong> {selectedProduct.special_standard}</Typography>
              <Typography variant="body1"><strong>입고일:</strong> {selectedProduct.date_received}</Typography>
              
            </Box>
          )}
        </Box>
      </Modal>
    </Box>
);
}

=======
import React from "react";

function ManageProduct() {
    return (
        <div>
        <h2>ManageProduct</h2>
        </div>
    );
    }
>>>>>>> e5f4478e466ed135085eb68ad645afc355701127
export default ManageProduct;