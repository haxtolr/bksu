import React, { useState, useEffect } from 'react';
import { useAuth } from '../components/AuthProvider.js';
import { Table, TableHead, TableRow, TableCell, TableBody, TableSortLabel, TextField, Card, CardHeader, CardContent, Collapse, IconButton, Box, Typography } from '@mui/material';
import Button from '@mui/material/Button';
import Switch from '@mui/material/Switch';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import ExpandMore from '@mui/icons-material/ExpandMore';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import config from '../components/config.js';
import "../styles/mpeople.css";

function ManagePeople() {
  const { authState } = useAuth();
  const [users, setUsers] = useState([]);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [editedUsers, setEditedUsers] = useState({});
  const [isModified, setIsModified] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [isTableVisible, setIsTableVisible] = useState(true);

  useEffect(() => {
    const fetchData = () => {
      fetch(`${config.baseURL}accounts/user_list/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${authState.token}`
        },
      })
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch((error) => {
        console.error('Error:', error);
      });
    };
    fetchData(); // Initial fetch
    const intervalId = setInterval(fetchData, 3000); // Fetch every 3 seconds

    return () => clearInterval(intervalId); // Cleanup interval on unmount
  }, [authState.token]);

  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });
  };

  const handleEdit = (id, field, value) => {
    setEditedUsers(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        [field]: value
      }
    }));
    setIsModified(true);
  };

  const handleChange = (id, field) => (event) => {
    handleEdit(id, field, event.target.value);
  };

  const handleSwitchChange = (id, field) => (event) => {
    handleEdit(id, field, event.target.checked);
  };

  const handleSave = () => {
    Object.keys(editedUsers).forEach(id => {
      const updates = editedUsers[id];

      fetch(`${config.baseURL}accounts/user-update/${id}/`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${authState.token}`
        },
        body: JSON.stringify(updates)
      })
      .then(response => {
        if (!response.ok) {
          return response.json().then(error => {
            throw new Error('Network response was not ok.');
          });
        }
        return response.json();
      })
      .then(data => {
        setUsers(prevUsers => prevUsers.map(user => user.id === data.id ? data : user));
        setIsModified(false);
        setEditedUsers({});
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    });
  };

  const sortedUsers = React.useMemo(() => {
    let sortableUsers = [...users];
    if (sortConfig.key !== null) {
      sortableUsers.sort((a, b) => {
        let aValue = a[sortConfig.key];
        let bValue = b[sortConfig.key];

        if (typeof aValue === 'boolean') {
          aValue = aValue ? 1 : 0;
          bValue = bValue ? 1 : 0;
        }

        if (aValue < bValue) {
          return sortConfig.direction === 'asc' ? -1 : 1;
        }
        if (aValue > bValue) {
          return sortConfig.direction === 'asc' ? 1 : -1;
        }
        return 0;
      });
    }
    return sortableUsers;
  }, [users, sortConfig]);

  const filteredUsers = sortedUsers.filter(user => {
    const searchValue = searchQuery.toLowerCase();
    return (
      user.id.toString().includes(searchValue) ||
      user.name.toLowerCase().includes(searchValue) ||
      user.rank.toLowerCase().includes(searchValue) ||
      user.phone.toLowerCase().includes(searchValue) ||
      user.username.toLowerCase().includes(searchValue)
    );
  });

  return (
    <Box sx={{ maxWidth: '100%', mx: 'auto', py: 4, px: 2 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4" component="h1" fontWeight="bold">
          인적 사항 관리
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <TextField
            label="검색"
            variant="outlined"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          <Button
            style={{
              backgroundColor: isModified ? 'green' : 'plum',
              color: 'white',
              padding: '10px 20px',
              fontSize: '20px'
            }}
            variant="contained"
            onClick={handleSave}
          >
            수정 완료
          </Button>
        </Box>
      </Box>
      <Card>
          <CardHeader
            title="All Users"
            sx={{ bgcolor: 'background.default' }}
            action={
              <IconButton onClick={() => setIsTableVisible(prev => !prev)}>
                <ExpandMore />
              </IconButton>
            }
          />
        <Collapse in={isTableVisible}>
          
          <CardContent>
            <Table>
              <TableHead className="bg-gray-200">
                <TableRow>
                  {['사번', '이름', '직급', '전화번호', 'ID', '주간', '일간', '최근 로그인시간', 'TEST', '접속중', '관리자 권한', '가입 승인'].map((key, index) => (
                    <TableCell key={index} style={{ whiteSpace: 'nowrap' }}>
                      <TableSortLabel
                        IconComponent={props => <ArrowDropDownIcon {...props} style={{ fontSize: '1rem' }} />}
                        active={sortConfig.key === key}
                        direction={sortConfig.direction}
                        onClick={() => handleSort(key)}
                      >
                        {key}
                      </TableSortLabel>
                    </TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {filteredUsers.map((user, index) => (
                  <TableRow key={index}>
                    <TableCell>{user.id}</TableCell>
                    <TableCell>{user.name}</TableCell>
                    <TableCell onDoubleClick={() => handleEdit(user.id, 'rank', prompt('Enter new rank:', user.rank))}>
                      {editedUsers[user.id] && editedUsers[user.id].rank ? editedUsers[user.id].rank : user.rank}
                    </TableCell>
                    <TableCell onDoubleClick={() => handleEdit(user.id, 'phone', prompt('Enter new phone number:', user.phone))}>
                      {editedUsers[user.id] && editedUsers[user.id].phone ? editedUsers[user.id].phone : user.phone}
                    </TableCell>
                    <TableCell>{user.username}</TableCell>
                    <TableCell>{Math.floor(user.week_time / 60)}시간 {user.week_time%60}분</TableCell>
                    <TableCell>{Math.floor(user.day_time / 60)}시간 {user.day_time%60}분</TableCell>
                    <TableCell>{new Date(user.login_time).toLocaleTimeString()}</TableCell>
                    <TableCell>버튼 넣기</TableCell>
                    <TableCell>
                      {user.is_active ? (
                        <CheckCircleIcon style={{ color: 'green' }} />
                      ) : (
                        <CancelIcon style={{ color: 'red' }} />
                      )}
                    </TableCell>
                    <TableCell>
                      <Switch
                        checked={editedUsers[user.id] && editedUsers[user.id].is_staff !== undefined ? editedUsers[user.id].is_staff : user.is_staff}
                        onChange={handleSwitchChange(user.id, 'is_staff')}
                      />
                    </TableCell>
                    <TableCell>
                      <Button
                        variant="contained"
                        color={editedUsers[user.id] && editedUsers[user.id].is_approved ? "primary" : "secondary"}
                        onClick={() => handleEdit(user.id, 'is_approved', !(user.is_approved))}
                      >
                        {user.is_approved ? '승인' : '미승인'}
                      </Button>
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

export default ManagePeople;
