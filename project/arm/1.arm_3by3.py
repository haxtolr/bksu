from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
import queue
import threading

# 색상별로 처리할 횟수를 저장하는 변수
g = 1
p = 1
o = 1 
y = 1
# MyCobot 객체 생성
mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)

# 쓰레드 간 결과를 공유하기 위한 큐
result_queue = queue.Queue()

# 그립 초기화
mc.set_gripper_mode(0)
mc.init_eletric_gripper()
mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1)

# 색상을 찾아내는 함수
def color_detect(frame):
    # BGR에서 HSV로 색상 공간 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 초록색 범위
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
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
    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([170, 255, 255])
    purple_mask = cv2.inRange(hsv, lower_purple, upper_purple) 

    # 각 색상별로 마스크를 적용하고, 결과 영상에서 픽셀 수를 세어 가장 큰 영역을 가진 색상을 찾기.
    masks = [("green", green_mask), ("yellow", yellow_mask), ("orange", orange_mask), ("purple", purple_mask)]
    max_color = max(masks, key=lambda x: cv2.countNonZero(x[1]))
    # 외곽선 찾기
    result = max_color[0] if cv2.countNonZero(max_color[1]) > 500 else "none"
    # 결과 큐에 결과를 저장
    result_queue.put(result)
    # 가장 큰 외곽선 찾기
    return max_color[0] 

# time.sleep을 쓰래드로 사용하기 위한 함수
def time_sleep():
    sleep_thread = threading.Thread(target=time.sleep, args=(2,))
    sleep_thread.start()
    sleep_thread.join()  


# 색상별로 처리하는 함수
def handel_base(result):
    mc.send_coords([204, -5.5, 350, -178, -0.69, 0.44], 70, 1) # 보러가는거
    print("보러가기")
    time_sleep()
    mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 70, 1) # 보러가는거
    print("보러가기2")
    time_sleep()
    mc.send_coords([281.45, 32.8, 273.9, -179.21, -2.55, -3.1], 70, 1) #잡으러
    print("잡으러")
    time_sleep()
    mc.set_eletric_gripper(1) #닫기
    mc.set_gripper_value(34, 20, 1) 
    print("닫기")
    time_sleep()
    mc.send_coords([251.45, 40, 333.9, -179.21, -2.55, -3.1], 70, 0) # 잡고 살짝들고
    print("잡고 살짝들기")
    time_sleep()
    if result == "green":
        print("green")
        handle_green()
    elif result == 'yellow':
        print("yellow")
        handle_yellow()
    elif result == 'orange':
        print("orange")
        handle_orange()
    elif result == 'purple':
        print("purple")
        handle_purple()
    mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 70, 1) # 보러가는거
    time_sleep()


# 색상별로 처리하는 함수
def handle_green():
    global g
    print("Handling green color")
    mc.send_coords([4, 278, 302, -176.47, -0.35, 0.47], 70, 1)
    time_sleep()
    if g == 1:
        mc.send_coords([4, 278, 160, -176.47, -0.35, 0.47], 70, 1)
        time_sleep() # g1
    if g == 2:
        mc.send_coords([4, 278, 194.3, -176.47, -0.35, 0.47], 70, 1)
        time_sleep() # g2
    if g == 3:
        mc.send_coords([4, 278, 221.3, -176.47, -0.35, 0.47], 70, 1)
        time_sleep() #g3
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(80, 40, 1) # 여는거
    time_sleep()
    mc.send_coords([4, 278, 302, -176.47, -0.35, 0.47], 70, 1)
    time_sleep()
    g = g + 1
    print("green : ", g)

def handle_purple():
    global p
    print("Handling purple color")
    mc.send_coords([80, 278, 302, -176.47, -0.35, 0.47], 70, 1) # p0
    time_sleep()
    if p == 1:
        mc.send_coords([80, 278, 160.3, -176.47, -0.35, 0.47], 70, 1) # p1
        time.sleep(3)
    if p == 2:
        mc.send_coords([80, 278, 180.3, -176.47, -0.35, 0.47], 70, 1) # p2
        time.sleep(3)
    if p == 3:
        mc.send_coords([80, 278, 200.3, -176.47, -0.35, 0.47], 70, 1) # p3
        time.sleep(3)
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(80, 40, 1) # 여는거
    time_sleep()
    mc.send_coords([80, 278, 302, -176.47, -0.35, 0.47], 70, 1)
    time_sleep()
    p = p + 1
    print("purple : ", p)

def handle_orange():
    global o
    print("Handling orange color")
    mc.send_coords([136, 251, 302, -175.87, -0.21, -7.56], 70, 1) # o0
    time_sleep()
    if o == 1:
        mc.send_coords([136, 251, 160.3, -175.87, -0.21, -7.56], 70, 1) # o1
        time_sleep()
    if o == 2:
        mc.send_coords([136, 251, 194.3, -175.87, -0.21, -7.56], 70, 1) # o2
        time_sleep()
    if o == 3:
        mc.send_coords([136, 251, 221.3, -175.87, -0.21, -7.56], 70, 1) # 03.
        time_sleep()
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(80, 40, 1) # 여는거
    time_sleep()
    mc.send_coords([136, 251, 302, -175.87, -0.21, -7.56], 70, 1) # o0
    time_sleep()
    o = o + 1
    print("orange : ", o)
    
def handle_yellow():
    global y
    print("Handling yellow color")
    mc.send_coords([172, 87, 399.7, -170, -13, -6], 70, 1) # y0
    time_sleep()
    if y == 1:
        mc.send_coords([218, 264, 164.7, -180, 1, -7], 70, 1) # y1
        time_sleep()
    if y == 2:
        mc.send_coords([218, 264, 198.7, -180, 1, -7], 70, 1) # y2
        time_sleep()
    if y == 3:
        mc.send_coords([218, 264, 232.7, -180, 1, -7], 70, 1) # y3
        time_sleep()
    mc.set_eletric_gripper(0)
    mc.set_gripper_value(80, 40, 1) # 여는거
    time_sleep()
    mc.send_coords([172, 87, 399.7, -170, -13, -6], 70, 1) # y0
    time_sleep()
    y = y + 1
    print("yellow : ", y)

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 비디오 프레임의 너비와 높이를 설정    
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 명도 조절을 위한 변수
contrast_factor = 1.5

# 쓰레드 객체 유무를 저장하는 변수
thread = None
moving = True

catch_cam = [204, -5.5, 310, -178, -0.69, 0.44] # 색을 인식하러 가는 좌표
mc.send_coords([204, -5.5, 315, -178, -0.69, 0.44], 70, 0) # 보러가는거
time_sleep()

# 비디오 프레임을 읽어오는 루프
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
    width = frame.shape[1]

     # 왼쪽과 오른쪽으로 약 10% 정도 프레임을 잘라낸다.
    cropped_frame = frame[:, int(width*0.1):int(width*0.9)]

    cv2.imshow('frame', cropped_frame)
    
    # 로봇이 움직이고 있는지 확인
    coords = mc.get_coords()
    if coords is None:
        continue
    else:
        coords = np.array(mc.get_coords())
        margin = 0.5
        lower_bounds = coords - margin
        upper_bounds = coords + margin

    if np.any((lower_bounds <= catch_cam) & (catch_cam <= upper_bounds)):
        print(coords)
        moving = False
    else:
        moving = True
        print(coords)

    if moving == False:  # 쓰레드를 시작할 조건
        time_sleep()
        if thread is None or not thread.is_alive():  # 쓰레드가 아직 시작되지 않았거나 이미 종료되었다면
            thread = threading.Thread(target=color_detect, args=(frame, ))  # 새로운 쓰레드를 생성하고
            thread.start()  # 시작
            print("thread start")
            thread.join()
            moving = True

    # 색상찾고 해야될 동작
    if not result_queue.empty():
        result = result_queue.get()
        if result != "none":
            handel_base(result)
            thread.join()
            moving = False

    if moving == True and not result_queue.empty():  # 쓰레드를 종료할 조건
        if thread is not None and thread.is_alive():  # 쓰레드가 실행 중이라면 쓰레드 종료
            thread.join()
            print("thread end")
            moving = False
    if o == 4 and p == 4 and g == 4: # 모든 색상을 다 처리했을 때 종료
        break
    


cap.release()
cv2.destroyAllWindows()

