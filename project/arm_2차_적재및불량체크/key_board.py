from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
from pynput import keyboard


mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)
#mc.send_angles([0, 0, 0, 0, 0, 0], 30)
#time.sleep(5)

mc.set_gripper_mode(0)
mc.init_eletric_gripper()

def on_press(key):
    try:
        # 'o'를 누르면 그리퍼가 열립니다.
        if key.char == 'o':
            mc.set_eletric_gripper(0)
            mc.set_gripper_value(80, 20, 1)

        # 'p'를 누르면 그리퍼가 닫힙니다.
        elif key.char == 'p':
            mc.set_eletric_gripper(1)
            mc.set_gripper_value(20, 20, 1)

        elif key.char == 'q':
            mc.set

    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

