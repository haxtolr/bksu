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

const ManageHome = () => {
  const { authState } = useAuth();
  const [agvData, setAgvData] = useState([]);
  const [rackData, setRackData] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [selectedItem, setSelectedItem] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const requestConfig = {
        headers: { 'Authorization': `Token ${authState.token}` }
      };  
      const agvResult = await axios(`${config.baseURL}api/agv`, requestConfig);
      const rackResult = await axios(`${config.baseURL}api/racks`, requestConfig);
      setAgvData(agvResult.data);
      setRackData(rackResult.data);
    };
  
    fetchData();
  }, [authState.token]);
  console.log(agvData);
  console.log(rackData);

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

  const handleOpenModal = (item) => {
    setSelectedItem(item);
    setModalOpen(true);
  };

  const handleCloseModal = () => {
    setModalOpen(false);
  };

      return (
        <div className="flex h-screen w-full">
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
                      <div key={index} className="bg-[#FFFDFE] rounded-lg shadow-md p-6" onClick={() => handleOpenModal(item)}>
                        <h3 className="text-lg font-bold mb-4 text-gray-900">{item.id}번 AGV</h3>
                        <div className="flex items-center justify-center">
                        <div className={`w-16 h-16 rounded-full ${statusColor(item.status)}`}></div>
                        </div>
                        <button onClick={() => handleOpenModal(item)}><InfoIcon /></button>
                      </div>
                    ))}
                  </div>
                  <Modal
                    open={modalOpen}
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
                      <div style={{ flex: 1 }}>
                        <iframe title="AGV Video" src="http://172.30.1.5:8080/?action=stream" width="640" height="320" style={{ border: '2px solid black', borderRadius: '10px' }}></iframe>
                      </div>
                    </Box>
                  </Modal>
                </div>
                <div className="bg-[#FFF1F1] p-4 rounded-lg shadow-md">
                  <h2 className="text-lg font-bold mb-4 text-gray-900">RACK</h2>
                  <div className="grid grid-cols-2 gap-4">
                    {rackData.map((item, index) => (
                      <div key={index} className="bg-[#FFFDFE] rounded-lg shadow-md p-6" onClick={() => handleOpenModal(item)}>
                        <h3 className="text-lg font-bold mb-4 text-gray-900">{item.id}번 RACK</h3>
                        <div className="flex items-center justify-center">
                          <div className={`w-16 h-16 rounded-full ${statusColor(item.status)}`}></div>
                        </div>
                            <button onClick={() => handleOpenModal(item)}><InfoIcon /></button>
                      </div>
                    ))}
                  </div>
                  <Modal
                    open={modalOpen}
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
                      <div style={{ flex: 1 }}>
                        <iframe title="AGV Video" src="http://172.30.1.73:8080/?action=stream" width="640" height="320" style={{ border: '2px solid black', borderRadius: '10px' }}></iframe>
                      </div>
                    </Box>
                  </Modal>
                </div>
              </div>
            </div>
          </main>
        </div>
    );
}
  export default ManageHome;













//function ManageHome() {
//    //const { authState } = useAuth();  // authState 가져오기
//    //const history = useHistory();

//    //useEffect(() => {
//    //    // is_staff가 true가 아니면 로그인 페이지로 리다이렉트
//    //    if (!authState.is_staff) {
//    //        history.push('/login');
//    //    }
//    //}, [authState, history]);

//    return (
//        <div className="flex h-screen w-full">
//          <main className="flex-1 bg-gray-100 dark:bg-gray-900">
//            <div className="container mx-auto py-8 px-4 md:px-6 lg:px-8">
//              <h1 className="text-2xl font-bold mb-6 text-gray-900 dark:text-gray-100">관리자 페이지</h1>
//              <div className="grid grid-cols-3 gap-6">
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">AGV1</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-green-500 dark:bg-green-600" />
//                  </div>
//                </div>
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">AGV2</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-green-500 dark:bg-green-600" />
//                  </div>
//                </div>
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">AGV3</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-red-500 dark:bg-red-600" />
//                  </div>
//                </div>
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">RACK1</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-green-500 dark:bg-green-600" />
//                  </div>
//                </div>
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">RACK2</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-red-500 dark:bg-red-600" />
//                  </div>
//                </div>
//                <div className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
//                  <h2 className="text-lg font-bold mb-4 text-gray-900 dark:text-gray-100">RACK3</h2>
//                  <div className="flex items-center justify-center">
//                    <div className="w-16 h-16 rounded-full bg-green-500 dark:bg-green-600" />
//                  </div>
//                </div>
//              </div>
//            </div>
//          </main>
//        </div>
//      )
//    }

//export default ManageHome;