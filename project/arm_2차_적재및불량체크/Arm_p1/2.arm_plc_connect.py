from pymycobot.mycobot import MyCobot
import cv2
import numpy as np
import time
from pynput import keyboard
import queue
import threading
import socket

HOST = '172.30.1.67'
PORT = 8081

msg_send = None # 클라이언트에서 보낼 메시지
msg_recv = None # 서버에서 받은 메시지

g = 1
p = 1
o = 1 
y = 1

mc = MyCobot('/dev/tty.usbserial-56E30046941', 115200)

result_queue = queue.Queue()

mc.set_gripper_mode(0)
mc.init_eletric_gripper()

mc.set_eletric_gripper(1)
mc.set_gripper_value(20, 20, 1)
time.sleep(4)
mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1)

def color_detect(frame): # 색상을 찾는 함수
    global msg_send   
    # BGR에서 HSV로 색상 공간 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 초록색 범위
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 노란색 범위
    lower_yellow = np.array([20, 125, 125])
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
    contours, _ = cv2.findContours(max_color[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 가장 큰 외곽선 찾기
    max_contour = max(contours, key=cv2.contourArea, default=None)

    # 가장 큰 외곽선 찾기
    if max_contour is not None:
        rect = cv2.minAreaRect(max_contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        
        # 사각형의 너비와 높이를 계산합니다.
        w, h = rect[1]
        if w == 0 or h == 0:
            ratio = 10
        if w != 0 and h != 0:
            ratio = w / float(h) # 비율 계산
        if ratio < 0.4 or ratio > 1.3:
            result = "none"
            msg_send = "N"
            return "N"
        else:
            if cv2.countNonZero(max_color[1]) > 500: # 500 이상인 외곽선만 선택
               result = max_color[0]
            else:
                result = "none"
                msg_send = "N"
    else:
        result = "none"
        msg_send = "N"


    result_queue.put(result)

    return max_color[0] 

def time_sleep(): # 시간 지연 함수
    sleep_thread = threading.Thread(target=time.sleep, args=(3,))
    sleep_thread.start() 
    sleep_thread.join()  

def handle_green(): # 초록색 처리 함수
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

def handle_purple(): # 보라색 처리 함수
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

def handle_orange(): # 오렌지색 처리 함수
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
    
def handle_yellow(): # 노란색 처리 함수
    global y

    if y < 4:
        print("Handling yellow color")
        mc.send_coords([136, 251, 302, -175.87, -0.21, -7.56], 70, 1) # y0
        time_sleep()
        if y == 1:
            mc.send_coords([218, 264, 164, -180, 1, -7], 70, 1) # y1 # y1
            time_sleep()
        if y == 2:
            mc.send_coords([218, 264, 194.7, -180, 1, -7], 70, 1) # y2
            time_sleep()
        if y == 3:
            mc.send_coords([218, 264, 228.7, -180, 1, -7], 70, 1) # y3
            time_sleep()
        mc.set_eletric_gripper(0)
        mc.set_gripper_value(80, 40, 1) # 여는거
        time_sleep()
        mc.send_coords([172, 87, 399.7, -170, -13, -6], 70, 1) # y0
        time_sleep()
        y = y + 1
        print("yellow : ", y)

def handel_base(result): # 색상에 따라 처리 함수
    global msg_send, send_thread, o, p, g, y, msg_recv

    msg_send = result
    if send_thread is None or not send_thread.is_alive():  # 쓰레드가 없거나 쓰레드가 종료된 경우
        send_thread = threading.Thread(target=ft_send)  # 새로운 쓰레드 생성
        send_thread.start()
    if result == "yellow" and y == 5:
        return
    if result == "purple" and p == 5:
        return
    if result == "orange" and o == 5:
        return
    if result == "green" and g == 5:
        return
    mc.send_coords([204, -5.5, 350, -178, -0.69, 0.44], 60, 1) # 보러가는거
    print("보러가기")
    time_sleep()
    mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 60, 1) # 보러가는거
    print("보러가기2")
    time_sleep()
    mc.send_coords([281.45, 32.8, 283.9, -179.21, -2.55, -3.1], 40, 1) #잡으러
    print("잡으러")
    time.sleep(2)
    mc.set_eletric_gripper(1) #닫기
    mc.set_gripper_value(34, 20, 1) 
    print("닫기")
    time_sleep()
    mc.send_coords([251.45, 40, 333.9, -179.21, -2.55, -3.1], 60, 0) # 잡고 살짝들고
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
    msg_recv = "wait"
    msg_send = "done"
    if send_thread is None or not send_thread.is_alive():  # 쓰레드가 없거나 쓰레드가 종료된 경우
        send_thread = threading.Thread(target=ft_send)  # 새로운 쓰레드 생성
        send_thread.start()
    mc.send_coords([204, -5.5, 310, -178, -0.69, 0.44], 40, 1)
    time_sleep()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 객체 생성
s.connect((HOST, PORT)) # 서버에 연결
con_msg = "연결 성공"

def ft_send(): # 소켓으로 데이터를 보내는 함수
    global msg_send

    while True:
        if msg_send is not None:
            s.sendall(msg_send.encode())
            msg_send = None
            break

def ft_recv(): # 소켓으로 데이터를 받는 함수
    global msg_recv
    global g, p, o, y

    while True:
        data = s.recv(1024)  # 서버에서 데이터 받기
        msg_recv = data.decode()
        if data.decode() == 'ny':
            print('버리는 색은 노란색입니다. ', repr(data.decode()))  # 받은 데이터 출력
            y = 5
        elif data.decode() == 'ng':
            print('버리는 색은 초록색입니다. ', repr(data.decode()))  # 받은 데이터 출력
            g = 5
        elif data.decode() == 'no':
            print('버리는 색은 오렌지색입니다. ', repr(data.decode()))
            o = 5
        elif data.decode() == 'np':
            print('버리는 색은 보라색입니다. ', repr(data.decode()))
            p = 5
        elif data.decode() == 'x':
            print('버리는 작업을 하지 않습니다.' , repr(data.decode()))
        elif data.decode() == 'b':
            print('물건이 라인에 도착했습니다.' , repr(data.decode()))
            msg_recv = 'b'
        elif data.decode() == 'ok':
            print('레일이 작업이 끝났습니다.' , repr(data.decode()))
        else:
            continue

send_thread = threading.Thread(target=ft_send)
recv_thread = threading.Thread(target=ft_recv)

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

mc.set_eletric_gripper(0)
mc.set_gripper_value(80, 20, 1) # 여는거

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

contrast_factor = 1.5

thread = None
moving = True


catch_cam = [204, -5.5, 310, -178, -0.69, 0.44]
mc.send_coords([204, -5.5, 315, -178, -0.69, 0.44], 40, 0) # 보러가는거
time_sleep()
recv_thread.start()

while True: # 물건이 라인에 도착할 때까지 대기
    if msg_recv == 'b':
        break

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
    
    coords = mc.get_coords() 
    if coords is None: 
        continue
    else:
        coords = np.array(mc.get_coords()) # 현재 좌표를 받아옴
        margin = 0.5
        lower_bounds = coords - margin
        upper_bounds = coords + margin

    if np.any((lower_bounds <= catch_cam) & (catch_cam <= upper_bounds)): # 현재 좌표와 목표 좌표가 일치하면
        moving = False
    else:
        moving = True

    if moving == False and msg_recv == 'b':  # 쓰레드를 시작할 조건
        time_sleep()
        if thread is None or not thread.is_alive():  # 쓰레드가 아직 시작되지 않았거나 이미 종료되었다면
            thread = threading.Thread(target=color_detect, args=(frame, ))  # 새로운 쓰레드를 생성하고
            thread.start() # 시작
            print("thread start")
            thread.join()
            moving = True
    if msg_send == "N" and result_queue.empty() == "none": # 불량일때
        print("불량품")
        if send_thread is None or not send_thread.is_alive():
            send_thread = threading.Thread(target=ft_send)
            send_thread.start()

    if not result_queue.empty(): # 결과 큐에 값이 있을 때
        result = result_queue.get() # 결과를 가져옴
        if result != "none": # 결과가 none이 아닐 때
            handel_base(result) # 결과에 따라 처리 함수 호출
            moving = False
    msg_recv = None

    if moving == False: #
        if send_thread is None or not send_thread.is_alive():
            send_thread = threading.Thread(target=ft_send)
            send_thread.start()
        msg_send = "done"

    if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 종료
        break

    if o > 3 and p > 3 and g > 3 and y > 3: # 모든 색상을 처리했을 때
        msg_send = "end" # end 메시지를 보냄
        if send_thread is None or not send_thread.is_alive():
            send_thread = threading.Thread(target=ft_send)
            send_thread.start()
        break

cap.release()
cv2.destroyAllWindows()