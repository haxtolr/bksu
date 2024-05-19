import React, { useState, useEffect } from 'react';
import { useAuth } from '../components/AuthProvider.js';
import { Table, TableHead, TableRow, TableCell, TableBody, TableSortLabel, TextField } from '@mui/material';
import Button from '@mui/material/Button';
import Switch from '@mui/material/Switch';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import config from '../components/config.js';
import "../styles/mpeople.css";
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';

function ManagePeople() {
  const { authState } = useAuth();
  const [users, setUsers] = useState([]);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [editedUsers, setEditedUsers] = useState({});
  const [isModified, setIsModified] = useState(false);

  useEffect(() => {
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
      
      console.log(updates);
      fetch(`${config.baseURL}accounts/user-update/${id}/`, {
        method: 'PATCH', // Use PATCH for partial updates
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${authState.token}`
        },
        body: JSON.stringify(updates)
      })
      .then(response => {
        if (!response.ok) {return response.json().then(error => {
          throw new Error('Network response was not ok.');
        });
      }
        return response.json();
      })
      .then(data => {
        // Update the local state to reflect the changes
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

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-4xl font-bold">인적 사항 관리</h1>
        <div className="flex items-center space-x-4">
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
        </div>
      </div>
      <div className="overflow-x-auto" style={{ backgroundColor: 'white', borderRadius: '10px' }}>
        <Table>
          <TableHead className="bg-gray-100">
            <TableRow>
              {['id', 'name', 'rank', 'phone', 'username', 'week_time', 'day_time', 'login_time', ,'TEST','is_active', 'is_staff', 'is_approved'].map((key, index) => (
                <TableCell key={index}>
                  {['is_active', 'is_staff', 'is_approved'].includes(key) ? (
                    <TableSortLabel
                      IconComponent={props => <ArrowDropDownIcon {...props} style={{ fontSize: '1rem' }} />}
                      active={sortConfig.key === key}
                      direction={sortConfig.direction}
                      onClick={() => handleSort(key)}
                    >
                      {key}
                    </TableSortLabel>
                  ) : (
                    <TableSortLabel
                      IconComponent={props => <ArrowDropDownIcon {...props} style={{ fontSize: '1rem' }} />}
                      active={sortConfig.key === key}
                      direction={sortConfig.direction}
                      onClick={() => handleSort(key)}
                    >
                      {key}
                    </TableSortLabel>
                  )}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {sortedUsers.map((user, index) => (
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
                <TableCell>{new Date(user.week_time).toLocaleTimeString()}</TableCell>
                <TableCell>{new Date(user.day_time).toLocaleTimeString()}</TableCell>
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
      </div>
    </div>
  );
}

export default ManagePeople;
