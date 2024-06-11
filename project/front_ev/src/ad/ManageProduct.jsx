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
      <Box sx={{ display: 'grid', gap: 3, mt: 4, gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))' }}>
        <Card>
          <CardHeader title="Sales Trends" />
          <CardContent>
            <LineChart />
          </CardContent>
        </Card>
        <Card>
          <CardHeader title="Inventory Levels" />
          <CardContent>
            <BarChart />
          </CardContent>
        </Card>
        <Card>
          <CardHeader title="Top Selling Products" />
          <CardContent>
            <PieChart />
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

function BarChart(props) {
  return (
    <Box {...props}>
      <ResponsiveBar
        data={[
          { name: 'Jan', count: 111 },
          { name: 'Feb', count: 157 },
          { name: 'Mar', count: 129 },
          { name: 'Apr', count: 150 },
          { name: 'May', count: 119 },
          { name: 'Jun', count: 72 },
        ]}
        keys={['count']}
        indexBy="name"
        margin={{ top: 20, right: 20, bottom: 50, left: 60 }}
        padding={0.3}
        colors={['#2563eb']}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: 'Month',
          legendPosition: 'middle',
          legendOffset: 32,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: 'Count',
          legendPosition: 'middle',
          legendOffset: -40,
        }}
        gridYValues={4}
        theme={{
          tooltip: {
            container: {
              fontSize: '12px',
            },
          },
        }}
        enableLabel={false}
        role="application"
        ariaLabel="Bar chart representing inventory levels by month"
      />
    </Box>
  );
}

function LineChart(props) {
  return (
    <Box {...props}>
      <ResponsiveLine
        data={[
          {
            id: 'Desktop',
            data: [
              { x: 'Jan', y: 43 },
              { x: 'Feb', y: 137 },
              { x: 'Mar', y: 61 },
              { x: 'Apr', y: 145 },
              { x: 'May', y: 26 },
              { x: 'Jun', y: 154 },
            ],
          },
          {
            id: 'Mobile',
            data: [
              { x: 'Jan', y: 60 },
              { x: 'Feb', y: 48 },
              { x: 'Mar', y: 177 },
              { x: 'Apr', y: 78 },
              { x: 'May', y: 96 },
              { x: 'Jun', y: 204 },
            ],
          },
        ]}
        margin={{ top: 20, right: 20, bottom: 50, left: 60 }}
        xScale={{ type: 'point' }}
        yScale={{ type: 'linear', stacked: true, min: 'auto', max: 'auto' }}
        axisBottom={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: 'Month',
          legendPosition: 'middle',
          legendOffset: 32,
        }}
        axisLeft={{
          tickSize: 5,
          tickPadding: 5,
          tickRotation: 0,
          legend: 'Sales',
          legendPosition: 'middle',
          legendOffset: -40,
        }}
        colors={['#2563eb', '#e11d48']}
        pointSize={10}
        pointColor={{ theme: 'background' }}
        pointBorderWidth={2}
        pointBorderColor={{ from: 'serieColor' }}
        pointLabelYOffset={-12}
        useMesh={true}
        theme={{
          tooltip: {
            container: {
              fontSize: '12px',
            },
          },
        }}
        role="application"
        ariaLabel="Line chart representing sales trends"
      />
    </Box>
  );
}

function PieChart(props) {
  return (
    <Box {...props}>
      <ResponsivePie
        data={[
          { id: 'Jan', value: 111 },
          { id: 'Feb', value: 157 },
          { id: 'Mar', value: 129 },
          { id: 'Apr', value: 150 },
          { id: 'May', value: 119 },
          { id: 'Jun', value: 72 },
        ]}
        sortByValue={true}
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
        innerRadius={0.5}
        padAngle={0.7}
        cornerRadius={3}
        activeOuterRadiusOffset={8}
        borderWidth={1}
        borderColor={{ from: 'color', modifiers: [['darker', 0.2]] }}
        arcLinkLabelsSkipAngle={10}
        arcLinkLabelsTextColor="#333333"
        arcLinkLabelsThickness={2}
        arcLinkLabelsColor={{ from: 'color' }}
        arcLabelsSkipAngle={10}
        arcLabelsTextColor={{ from: 'color', modifiers: [['darker', 2]] }}
        theme={{
          tooltip: {
            container: {
              fontSize: '12px',
            },
          },
        }}
        role="application"
        ariaLabel="Pie chart representing top selling products"
      />
    </Box>
  );
}

export default ManageProduct;
