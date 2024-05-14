from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
from pynput import keyboard
import queue
import threading

def ft_mov_pos(ft_position):
    while True:
        mc.send_angles(ft_position, 30)
        print("moving")
        time.sleep(3)
        angles = mc.get_angles()
        if np.allclose(angles, ft_position, atol=0.8):
            print("done")
            return 1

green_cut = 0

mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)

result_queue = queue.Queue()

mc.set_gripper_mode(0)
mc.init_eletric_gripper()

mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1)

def color_detect(frame):
    # BGR에서 HSV로 색상 공간 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 초록색 범위
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 노랑색 범위
    lower_yellow = np.array([20, 150, 150])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 오렌지색 범위
    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([15, 255, 255])
    orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # 보라색 범위
    lower_purple = np.array([140, 50, 50])
    upper_purple = np.array([170, 255, 255])
    purple_mask = cv2.inRange(hsv, lower_purple, upper_purple) 

    # 각 색상별로 마스크를 적용하고, 결과 영상에서 픽셀 수를 세어 가장 큰 영역을 가진 색상을 찾기.
    masks = [("green", green_mask), ("yellow", yellow_mask), ("orange", orange_mask), ("purple", purple_mask)]
    max_color = max(masks, key=lambda x: cv2.countNonZero(x[1]))
    result = max_color[0] if cv2.countNonZero(max_color[1]) > 500 else "none"
    result_queue.put(result)
    
    return max_color[0] 

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

contrast_factor = 1.5

thread = None
moving = False

mc.send_coords([204, 10.4, 320, -178, -0.58, -4], 40, 1)
cpos = mc.get_coords()
print(cpos)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # RGB 색상 공간에서 HSV 색상 공간으로 변환.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # V 채널(명도)의 값을 조절하여 색상의 강도 낮춤.
    hsv[:,:,2] = hsv[:,:,2] * 0.8

    # HSV 색상 공간에서 RGB 색상 공간으로 변환
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame', frame)


    if moving == False:  # 쓰레드를 시작할 조건
        if thread is None or not thread.is_alive():  # 쓰레드가 아직 시작되지 않았거나 이미 종료되었다면
            thread = threading.Thread(target=color_detect, args=(frame, ))  # 새로운 쓰레드를 생성하고
            thread.start()  # 시작
            print("thread start")
            moving = True

    # 색상찾고 해야될 동작
    if not result_queue.empty():
        result = result_queue.get()
        cv2.putText(frame, result, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        if result == "green":
            print("green")
            moving = True
        elif result == 'yellow':
            print("yellow")
            moving = True
        elif result == 'orange':
            print("orange")
            moving = True
        elif result == 'purple':
            print("purple")
            moving = True

    if moving == True and not result_queue.empty():  # 쓰레드를 종료할 조건
        if thread is not None and thread.is_alive():  # 쓰레드가 실행 중이라면
            # 쓰레드를 종료. 이를 위해서는 쓰레드 함수 내에서 종료 조건을 확인하고,
            # 해당 조건이 만족되면 함수를 반환하여 쓰레드를 종료.
            thread.join()
            print("thread end")
            moving = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('a'):
        moving = False

cap.release()
cv2.destroyAllWindows()

