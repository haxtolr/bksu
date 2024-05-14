from PyQt5.QtWidgets import *
import sys
import threading
				
from myjoystick import MyJoystick

from PyQt5 import QtWidgets
import socket
import time
import struct
import numpy as np
import cv2
from PyQt5 import QtGui

import pickle

# HOST_RPI = '192.168.0.129'
# HOST_RPI = '192.168.0.57'
# HOST_RPI = '172.30.1.23'
HOST_RPI = '172.30.1.36'

PORT = 8089

client_cam = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_mot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_cam.connect((HOST_RPI, PORT))
client_mot.connect((HOST_RPI, PORT))

t_now = time.time()
t_prev = time.time()
cnt_frame = 0
total_frame = 0
cnt_time = 0

def camMain() :
	global t_now, t_prev, cnt_frame, total_frame, cnt_time

	width = 320
	height = 240
	label.resize(width, height)

	while True:	

		# 메세지 보내기
		cmd = 12
		cmd_byte = struct.pack('!B', cmd) # Big-endian 표시 0x12345678
		client_cam.sendall(cmd_byte)#

		# 영상 받기
		data_len_bytes = client_cam.recv(4)
		data_len = struct.unpack('!L', data_len_bytes) # 

		frame_data = client_cam.recv(data_len[0], socket.MSG_WAITALL)#
		
		frame = pickle.loads(frame_data)#
		# print(type(frame))
		# 영상 출력
		# np_data = np.frombuffer(frame, dtype='uint8')
		# frame = cv2.imdecode(np_data,1)
		# frame = cv2.rotate(frame,cv2.ROTATE_180)
		# frame2 = cv2.resize(frame, (320, 240))
		# frame2 = cv2.resize(frame, (640, 480))
		 
		# h,w,c = frame2.shape
		# qImg = QtGui.QImage(frame2.data, w, h, w*c, \
		# QtGui.QImage.Format_BGR888)#
  
		h,w,c = frame.shape
		qImg = QtGui.QImage(frame.data, w, h, w*c, QtGui.QImage.Format_BGR888)#  
  
		pixmap = QtGui.QPixmap.fromImage(qImg)
		label.setPixmap(pixmap)

		cnt_frame += 1
		t_now = time.time()
		if t_now - t_prev >= 1.0 :
			t_prev = t_now
			total_frame += cnt_frame
			cnt_time += 1
			print("frame count : %f, %d average : %f" \
			%(cnt_frame, cnt_time, total_frame/cnt_time))
			cnt_frame = 0
			
def cbJoyPos(joystickPosition) :
	posX, posY = joystickPosition
	# 자동차 방향
	right, left = -1, -1
	if posY < -0.5:
		right, left = 1, 1
		print('brake')
	elif posY < 0.5 and posY >= -0.5:
		if -0.5 <= posX <= 0.5 :
			right, left = 1, 1
			print('stop')
		elif posX < -0.5 : 
			right, left = 1, 0
			print('left')
		elif posX > 0.5 :
			right, left = 0, 1
			print('right')
	else : # -0.5 <= posY <= 0.15
		right, left = 0, 0
		print('foward')

	rl = right << 1 | left
	print(rl)
	rl_byte = struct.pack('!B',rl)
	client_mot.sendall(rl_byte)

# Create main application window
app = QApplication([])
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create Screen
label = QtWidgets.QLabel()
ml.addWidget(label,0,0)

# Create joystick
joystick = MyJoystick(cbJoyPos)
ml.addWidget(joystick,1,0)

camThread = threading.Thread(target=camMain)  # 쓰레드로 
camThread.start()

mw.show()

# Start Qt event loop 
sys.exit(app.exec_())