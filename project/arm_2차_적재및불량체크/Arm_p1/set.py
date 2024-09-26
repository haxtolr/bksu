from pymycobot.mycobot import MyCobot
import time
from pynput import keyboard

mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)

#A = 0
#def on_press(key):
#    global A

#    try:
#        if key.char == 'a':
#            mc.set_gripper_value(80, 20, 1)
#            A = 1
#        elif key.char == 's':
#            mc.set_gripper_value(34, 20, 1)
#    except AttributeError:
#        pass

mc.set_gripper_mode(0)
mc.init_eletric_gripper()
time.sleep(3)
mc.set_eletric_gripper(1)
mc.set_gripper_value(34, 20, 1)
time.sleep(3)

#mc.send_coords([218, 264, 210.7, -180, 1, -7], 70, 1) # y0
#time.sleep(3)
#if i == 1:
#    mc.send_coords([218, 264, 160, -180, 1, -7], 70, 1) # y1
#    time.sleep(3)
#if i == 2:
#    mc.send_coords([218, 264, 194.7, -180, 1, -7], 70, 1) # y2
#    time.sleep(3)
#mc.send_coords([218, 264, 228.7, -180, 1, -7], 70, 1) # y3

mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1)
time.sleep(3)


#while True:
#    mc.send_coords([80, 278, 302, -176.47, -0.35, 0.47], 70, 1) # p0
#    time.sleep(2)
#    mc.set_eletric_gripper(0)
#    mc.set_gripper_value(80, 20, 1)
#    time.sleep(5)
#    mc.set_eletric_gripper(1)
#    mc.set_gripper_value(34, 20, 1)
#    time.sleep(5)
#    while True:
#        if p == 1:
#            mc.send_coords([80, 278, 160.3, -176.47, -0.35, 0.47], 70, 1) # p1
#            time.sleep(3)
#            break
#        if p == 2:
#            mc.send_coords([80, 278, 180.3, -176.47, -0.35, 0.47], 70, 1) # p2
#            time.sleep(3)
#            break
#        if p == 3:
#            mc.send_coords([80, 278, 200.3, -176.47, -0.35, 0.47], 70, 1) # p3
#            time.sleep(3)
#            break
#        time.sleep(2)
#    mc.set_eletric_gripper(1)
#    mc.set_gripper_value(80, 20, 1)
#    p = p + 1
#    if p == 4:
#        break