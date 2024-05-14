from PyQt5.QtWidgets import *      # PyQt5.QtWidgets���� ���� QApplication, QStyleFactory, QMainWidow, QWidget, QGridLayout Ŭ����
import sys
				
from myjoystick import MyJoystick
			
def cbJoyPos(joystickPosition) :   # �ݹ� �Լ�, ���̽�ƽ ��ġ���� ���ڷ� �޾� ���
	print(joystickPosition)          # ��ǥ���� X, Y�࿡ ���Ͽ� -1���� 1 ����

# Create main application window
app = QApplication([])             # �������α׷� ��ü�� �� ������ ����
app.setStyle(QStyleFactory.create("Cleanlooks"))
mw = QMainWindow()
mw.setWindowTitle('RC Car Joystick')
mw.setGeometry(100, 100, 300, 200)

# Create and set widget layout
# Main widget container
cw = QWidget()                     # �� �����쿡 ���� ���� ����
ml = QGridLayout()
cw.setLayout(ml)
mw.setCentralWidget(cw)

# Create joystick
joystick = MyJoystick(cbJoyPos)    # ���̽�ƽ �ν��Ͻ� ����
ml.addWidget(joystick,0,0)

mw.show()                          # �����츦 ȭ�鿡 ǥ��

# Start Qt event loop 
sys.exit(app.exec_())              # ���콺, Ű����, Ÿ�̸� �� ó��