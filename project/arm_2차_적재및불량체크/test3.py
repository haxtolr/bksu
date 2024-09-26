from pymycobot.mycobot import MyCobot

import time

mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)


#mc.set_gripper_mode(0)
#mc.init_eletric_gripper()
#mc.set_eletric_gripper(0)
#mc.set_gripper_value(80, 20, 1)
#time.sleep(3)
#mc.set_eletric_gripper(1)
#mc.set_gripper_value(20, 20, 1)
#time.sleep(3)

mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1) # 여는거
catch_cam = [204, -5.5, 310, -178, -0.69, 0.44]

i = 1
while True:
    if i == 4:
        break    
    #mc.send_angles([0, 0, 0, 0, 0, 0], 10)
    mc.send_coords([204, -5.5, 350, -178, -0.69, 0.44], 20, 1)  # 보러가는거
    print("up")
    time.sleep(3)
    mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 20, 1)  # 보러가는거
    time.sleep(3)
    print("1")
    mc.send_coords([281.45, 32.8, 283.9, -179.21, -2.55, -3.1], 20, 1) #잡으러
    time.sleep(5)
    print("2")
#   
    mc.set_eletric_gripper(1) #닫기
    mc.set_gripper_value(34, 20, 1) 
    time.sleep(4)
    print("grip")
    mc.send_coords([251.45, 40, 333.9, -179.21, -2.55, -3.1], 10, 0) # 잡고 살짝들고
    print("up")
    time.sleep(3)
    # 그린 좌표
    if i == 1:
        mc.send_coords([80, 278, 160.3, -176.47, -0.35, 0.47], 10, 1)
    if i == 2:
        mc.send_coords([80, 278, 194.3, -176.47, -0.35, 0.47], 10, 1)
    if i == 3:
        mc.send_coords([80, 278, 221.3, -176.47, -0.35, 0.47], 10, 1)

    
    time.sleep(5)
    #
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(80, 20, 1) # 여는거
    #
    time.sleep(5)
    print("3")
    time.sleep(5)
    mc.send_coords([62, 96, 413, -101, 17, 13], 40, 1)
    print("4")
    time.sleep(4)
#    mc.send_coords([267, 20.4, 347, -172, -14, -4.01], 50, 1)
    i = i + 1




# 그린 좌표
    #if i == 1:
    #    mc.send_coords([4, 278, 160, -176.47, -0.35, 0.47], 70, 1) # g1
    #if i == 2:
    #    mc.send_coords([4, 278, 194.3, -176.47, -0.35, 0.47], 70, 1) # g2
    #if i == 3:
    #    mc.send_coords([4, 278, 221.3, -176.47, -0.35, 0.47], 70, 0) #g3
    
























##mc.send_coords([4, 278, 221.3, -176.47, -0.35, 0.47], 10, 1)
##pos = mc.get_coords()
##time.sleep(3)
#print("done")

#mc.set_eletric_gripper(1)
#mc.set_gripper_value(34, 20, 1)

#pos = mc.get_coords()
#print(pos)
#time.sleep(3)
###print("----")
#mc.send_coords([3.9, 278.5, 165, -176.36, -0.41, 0.38], 10, 1)
#pos = mc.get_coords()
#print("2번째 : %f, %f, %f" % (pos[0], pos[1], pos[2]))
#print(pos)
