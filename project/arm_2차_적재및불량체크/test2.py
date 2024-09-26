from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
from pynput import keyboard
import threading


mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)


#mc.set_gripper_mode(0)
#mc.init_eletric_gripper()
#mc.set_eletric_gripper(0)
#mc.set_gripper_value(80, 20, 1)
#time.sleep(3)
#mc.set_eletric_gripper(1)
#mc.set_gripper_value(20, 20, 1)
#time.sleep(3)


#mc.send_coords([204, -5.5, 350, -178, -0.69, 0.44], 40, 1)  # 보러가는거
#print("up")
#time.sleep(5)
#mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 40, 1)  # 보러가는거
#time.sleep(5)
#print("1")
#mc.send_coords([281.45, 32.8, 283.9, -179.21, -2.55, -3.1], 40, 1) #잡으러
#time.sleep(5)
#print("2")

##

#mc.set_eletric_gripper(0)
#mc.set_gripper_value(80, 20, 1)
##time.sleep(3)



mc.send_coords([204, -5.5, 350, -178, -0.69, 0.44], 20, 1)  # 보러가는거
print("up")
time.sleep(3)
mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 20, 1)  # 보러가는거
time.sleep(3)
print("1")

#mc.set_eletric_gripper(1) #닫기
#mc.set_gripper_value(34, 20, 1)
#time.sleep(3)
##mc.send_coords([218, 264, 302, -180, 1, -7], 30, 1)
##time.sleep(5)
##236.7
##mc.send_coords([203, 234, 167.4, -180, 0.61, -7], 30, 1)

#time.sleep(5)
#mc.set_eletric_gripper(0)
#mc.set_gripper_value(80, 20, 1)
#time.sleep(3)

#mc.send_coords([4, 278, 302, -176.47, -0.35, 0.47], 70, 1) # 그린 0

#mc.send_coords([136, 251, 170, -175.87, -0.21, -7.56], 30, 1)
#time.sleep(5)

#mc.send_coords([80, 278, 302, -176.47, -0.35, 0.47], 10, 1)
#mc.send_coords([87.2, 118.5, 412.67, -161.93, -26.21, 53.31], 10, 1)

#   
#time.sleep(3)
#print("grip")
#mc.send_coords([281.45, 32.8, 333.9, -179.21, -2.55, -3.1], 10, 0)

#print("move")
#mc.send_coords([251.45, 40, 333.9, -179.21, -2.55, -3.1], 10, 0)
##time.sleep(5)
#mc.send_coords([80, 278, 160, -176.47, -0.35, 0.47], 10, 1) # g1
#print(mc.get_coords())
#print("up")