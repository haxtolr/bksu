// manageorder.jsx
import React, { useState, useEffect } from 'react';
import {
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
} from '@mui/material';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import { ExpandMore } from '@mui/icons-material';
import config from '../components/config.js';
import { useAuth } from '../components/AuthProvider.js';

function ManageOrder({ authToken }) {
  const { authState } = useAuth();
  const [open, setOpen] = useState(false);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [orders, setorders] = useState([]);
  const [orderDirection, setOrderDirection] = useState('asc');
  const [orderByField, setOrderByField] = useState('order_number');

  const handleOpen = (product) => {
    setSelectedProduct(product);
    setOpen(true);
  };

  const handleToggle = () => {
    setOpen(!open);
  };

  useEffect(() => {
    fetch(`${config.baseURL}api/allorders/`, {
      headers: {
        'Authorization': `Token ${authState.token}`
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setorders(data);
      })
      .catch(error => console.error(error));
  }, []);

  const handleRequestSort = (property) => {
    const isAsc = orderByField === property && orderDirection === 'asc';
    setOrderDirection(isAsc ? 'desc' : 'asc');
    setOrderByField(property);
  };

  const sortedorders = orders.sort((a, b) => {
    if (a[orderByField] < b[orderByField]) {
      return orderDirection === 'asc' ? -1 : 1;
    }
    if (a[orderByField] > b[orderByField]) {
      return orderDirection === 'asc' ? 1 : -1;
    }
    return 0;
  });

  return (
    <Box sx={{ maxWidth: '1200px', mx: 'auto', py: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4" component="h1" fontWeight="bold">
          주문 관리
        </Typography>
      </Box>
      <Card>
        <CardHeader
          title="All Orders"
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
                      active={orderByField === 'order_number'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('order_number')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      주문 번호
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderByField === 'customer'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('customer')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      주문자
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderByField === 'products'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('products')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      주문 상품
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderByField === 'destination'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('destination')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      목적지
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderByField === 'order_accepted'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('order_accepted')}
                      IconComponent={ArrowDropDownIcon}
                    >
                       주문 상태
                    </TableSortLabel>
                  </TableCell>
                  <TableCell>
                    <TableSortLabel
                      active={orderByField === 'order.agv_id'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('order.agv_id')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      담당 AGV
                    </TableSortLabel>
                  </TableCell><TableCell>
                    <TableSortLabel
                      active={orderByField === 'order_time'}
                      direction={orderDirection === 'asc' ? 'asc' : 'desc'}
                      onClick={() => handleRequestSort('order_time')}
                      IconComponent={ArrowDropDownIcon}
                    >
                      주문 시간
                    </TableSortLabel>
                  </TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {sortedorders.map((order) => (
                  <TableRow key={order.id}>
                    <TableCell>{order.order_number}</TableCell>
                    <TableCell>{order.customer}</TableCell>
                    <TableCell onClick={() => handleOpen(order.products)}>
                      {order.products.map((product, index) => (
                        <div key={index}>
                          {product.name} ({product.quantity}개)
                        </div>
                      ))}
                    </TableCell>
                    <TableCell>{order.destination}</TableCell>
                    <TableCell> {order.order_accepted ? "주문 완료" : "주문 실패"}</TableCell>
                    <TableCell>{order.agv_id}</TableCell>
                    <TableCell>{new Intl.DateTimeFormat(
                    'ko-KR', {
                        year: 'numeric',
                        month: '2-digit',
                        day: '2-digit',
                        hour: '2-digit',
                        minute: '2-digit'
                    }).format(new Date(order.order_time))}
                    </TableCell>
                    </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Collapse>
      </Card>
    </Box>
  );
}

export default ManageOrder;