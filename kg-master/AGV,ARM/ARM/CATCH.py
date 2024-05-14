from pymycobot.mycobot import MyCobot

import time

i = 0

mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)
mc.send_angles([0, 0, 0, 0, 0, 0], 30)
time.sleep(5)
mc.set_gripper_mode(0)
mc.init_eletric_gripper()

mc.set_eletric_gripper(0)
mc.set_gripper_value(0,20,1)
mc.set_eletric_gripper(1)
mc.set_gripper_value(100,20,1)


mc.set_gripper_value(30,20,1)
time.sleep(3)
mc.set_gripper_value(100,20,1)

for i in range(1,4):
    print(i)
    time.sleep(3)
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(30,20,1)
    time.sleep(4)
    mc.send_angles([0, 0, 0, 0, 0, 0], 10)
    time.sleep(8)
    time.sleep(3)
    mc.set_eletric_gripper(1)
    time.sleep(3)
    mc.send_angles([10, 10, 0, 0, 0, 0], 10)
    time.sleep(10)
    

