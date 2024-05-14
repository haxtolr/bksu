from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
from pynput import keyboard


mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)
mc.send_angles([0, 0, 0, 0, 0, 0], 30)
time.sleep(5)

def on_press(key):
    try:
        if key.char == 'q':
            mc.release_all_servos()
            print("off")
        elif key.char == 'w':
            print("home")
            mc.power_on()
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    angles = mc.get_angleqs()
    pos = mc.get_coords()

    print("각")
    print(angles)
    time.sleep(1)
    print("-------------------")
    print("좌표")
    print(pos)
    time.sleep(1)
