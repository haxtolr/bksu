import React, { useState, useEffect } from 'react';
import { useAuth } from '../components/AuthProvider.js';
import InfoIcon from '@mui/icons-material/Info';
import config from '../components/config.js';
import axios from 'axios';
import { Modal } from '@mui/material';
import Backdrop from '@mui/material/Backdrop';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Grid from '@material-ui/core/Grid';

const ManageHome = () => {
  const { authState } = useAuth();
  const [agvData, setAgvData] = useState([]);
  const [rackData, setRackData] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [agvModalOpen, setAgvModalOpen] = useState(false); // AGV 모달 상태
  const [rackModalOpen, setRackModalOpen] = useState(false); // RACK 모달 상태
  const [selectedItem, setSelectedItem] = useState(null);
  const [userActive, setUserActive] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const requestConfig = {
        headers: { 'Authorization': `Token ${authState.token}` }
      };  
      const agvResult = await axios(`${config.baseURL}api/agv`, requestConfig);
      const rackResult = await axios(`${config.baseURL}api/racks`, requestConfig);
      const userActive = await axios(`${config.baseURL}accounts/user_active`, requestConfig);
      setUserActive(userActive.data);
      setAgvData(agvResult.data);
      setRackData(rackResult.data);
    };
  
    fetchData();
  }, [authState.token]);
  console.log(agvData);
  console.log(rackData);
  console.log(userActive);

  const statusColor = (status) => {
    switch (status) {
      case 'RD':
        return 'bg-yellow-500';
      case 'MA':
        return 'bg-red-500';
      default:
        return 'bg-green-500';
    }
  };

  const handleOpenAgvModal = (item) => {
    setSelectedItem(item);
    setAgvModalOpen(true);
  };

  const handleOpenRackModal = (item) => {
    setSelectedItem(item);
    setRackModalOpen(true);
  };
  const handleCloseModal = () => {
    setAgvModalOpen(false);
    setRackModalOpen(false);
  };

  return (
    <div className="flex h-full w-full">
      <main className="flex-1 bg-gray-100 ">
        <div className="container mx-auto py-8 px-4 md:px-6 lg:px-8">
          <div className="flex items-center mb-2">
            <h1 className="text-4xl font-bold mb-6 text-gray-900 text-right">관리자 페이지</h1>
            <div className="flex items-center mb-2 justify-end">
              <span className="h-4 w-4 rounded-full bg-red-500 inline-block mr-2 ml-12"></span>
              <span>유지 보수 중</span>
            </div>
            <div className="flex items-center mb-2 justify-end">
              <span className="h-4 w-4 rounded-full bg-green-500 inline-block mr-2 ml-12"></span>
              <span>작업 중</span>
            </div>
            <div className="flex items-center mb-2 justify-end">
              <span className="h-4 w-4 rounded-full bg-yellow-500 inline-block mr-2 ml-12"></span>
              <span>준비 중</span>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-6">
            <div className="bg-[#FFF1F1] p-4 rounded-lg shadow-md">
              <h2 className="text-lg font-bold mb-4 text-gray-900">AGV</h2>
              <div className="grid grid-cols-2 gap-4">
                {agvData.map((item, index) => (
                  <div key={index} className="bg-[#FFFDFE] rounded-lg shadow-md p-6" onClick={() => handleOpenAgvModal(item)}>
                    <h3 className="text-lg font-bold mb-4 text-gray-900">{item.id}번 AGV</h3>
                    <div className="flex items-center justify-center">
                      <div className={`w-16 h-16 rounded-full ${statusColor(item.status)}`}></div>
                    </div>
                    <button onClick={() =>handleOpenAgvModal(item)}><InfoIcon /></button>
                  </div>
                ))}
              </div>
              <Modal
                open={agvModalOpen}
                onClose={handleCloseModal}
                BackdropComponent={Backdrop}
                BackdropProps={{
                  timeout: 500,
                  style: { backgroundColor: 'rgba(0, 0, 0, 0.5)' }
                }}
              >
                <Box sx={{ 
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  transform: 'translate(-50%, -50%)',
                  width: 942, 
                  height: 390,
                  bgcolor: 'grey.100', 
                  border: '2px solid #000', 
                  boxShadow: 24, 
                  p: 4, 
                  display: 'flex',
                  borderRadius: '10px',
                  justifyContent: 'center',
                  alignItems: 'center'
                }}>
                  {selectedItem && (
                    <div style={{ flex: 1 }}>
                      <Paper elevation={3} style={{ padding: '20px', margin: '10px' }}>
                        <Typography variant="h4" component="div">
                          {selectedItem.id} 번 AGV
                        </Typography>
                        <Typography variant="body1" component="p" style={{ marginTop: '10px' }}>
                          현재 상태 : {selectedItem.status === 'RD' ? '준비' :
                          selectedItem.status === 'BH' ? '복귀' :
                          selectedItem.status === 'UL' ? '하역' :
                          selectedItem.status === 'TG' ? '이송' :
                          selectedItem.status === 'MA' ? '유지 보수' :
                          selectedItem.status} 중
                        </Typography>
                        <Typography variant="body1" component="p" style={{ marginTop: '10px' }}>
                          배터리 : {selectedItem.battery}%
                        </Typography>
                      </Paper>
                    </div>
                  )}
                  <div style={{ width: '640px', height: '390px', overflow: 'hidden' }}>
                    {selectedItem && selectedItem.agv_camera ? (
                      <img 
                        alt="AGV Video" 
                        src={selectedItem.agv_camera} 
                        width="100%" 
                        height="100%" 
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                      />
                    ) : (
                      <div>AGV 카메라 영상이 없습니다.</div>
                    )}
                  </div>
                </Box>
              </Modal>
            </div>
            <div className="bg-[#FFF1F1] p-4 rounded-lg shadow-md">
              <h2 className="text-lg font-bold mb-4 text-gray-900">RACK</h2>
              <div className="grid grid-cols-2 gap-4">
                {rackData.map((item, index) => (
                  <div key={index} className="bg-[#FFFDFE] rounded-lg shadow-md p-6" onClick={() => handleOpenRackModal(item)}>
                    <h3 className="text-lg font-bold mb-4 text-gray-900">{item.id}번 RACK</h3>
                    <div className="flex items-center justify-center">
                      <div className={`w-16 h-16 rounded-full ${statusColor(item.status)}`}></div>
                    </div>
                    <button onClick={() => handleOpenRackModal(item)}><InfoIcon /></button>
                  </div>
                ))}
              </div>
              <Modal
                open={rackModalOpen}
                onClose={handleCloseModal}
                BackdropComponent={Backdrop}
                BackdropProps={{
                  timeout: 500,
                  style: { backgroundColor: 'rgba(0, 0, 0, 0.5)' }
                }}
              >
                <Box sx={{ 
                  position: 'absolute',
                  top: '50%',
                  left: '50%',
                  transform: 'translate(-50%, -50%)',
                  width: 942, 
                  height: 390,
                  bgcolor: 'grey.100', 
                  border: '2px solid #000', 
                  boxShadow: 24, 
                  p: 4, 
                  display: 'flex',
                  borderRadius: '10px',
                  justifyContent: 'center',
                  alignItems: 'center'
                }}>
                  {selectedItem && (
                    <div style={{ flex: 1 }}>
                      <Paper elevation={3} style={{ padding: '20px', margin: '10px' }}>
                        <Typography variant="h4" component="div">
                          {selectedItem.id} 번 RACK
                        </Typography>
                        <Typography variant="body1" component="p" style={{ marginTop: '10px' }}>
                          현재 상태 : {selectedItem.status === 'RD' ? '준비' :
                          selectedItem.status === 'OP' ? '작업' :
                          selectedItem.status === 'MA' ? '유지 보수' :
                          selectedItem.status} 중
                        </Typography>
                      </Paper>
                    </div>
                  )}
                  <div style={{ width: '640px', height: '390px', overflow: 'hidden' }}>
                    <img 
                      alt="RACK Video" 
                      src="http://172.30.1.65:7120/?action=stream"
                      width="100%" 
                      height="100%" 
                      style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    />
                  </div>
                </Box>
              </Modal>
            </div>
          </div>
          <div>
            <Box marginTop={3}>
            <h2 className="text-lg font-bold mb-4 text-gray-900">작업 중인 직원</h2>
            <TableContainer component={Paper}>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>이름</TableCell>
                    <TableCell align="right">직급</TableCell>
                    <TableCell align="right">접속 시간</TableCell>
                    <TableCell align="right">일일 접속 기간</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {userActive.map((user) => (
                    <TableRow key={user.name}>
                      <TableCell component="th" scope="row">
                        {user.name}
                      </TableCell>
                      <TableCell align="right">{user.rank}</TableCell>
                      <TableCell align="right">
                      {
                        new Date(user.login_time).toLocaleDateString() + ' ' +
                        new Date(user.login_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                      }
                      </TableCell>
                      <TableCell align="right">{user.day_time}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
            </Box>
          </div>
          <div style={{position: 'relative', zIndex: 1 }}>
                <Box marginTop={3}>
                  <h2 className="text-lg font-bold mb-4 text-gray-900">CCTV</h2>
                  <Grid container spacing={3}>
                    <Grid item xs={6}>
                      <img src="http://172.30.1.65:7121/?action=stream" alt="CCTV 1" width="640" height="320" />
                    </Grid>
                    <Grid item xs={6}>
                      <img src="http://172.30.1.9:7122/?action=stream" alt="CCTV 2" width="640" height="320" />
                    </Grid>
                  </Grid>
                </Box>
              </div>
        </div>
      </main>
    </div>    
  );
};

export default ManageHome;