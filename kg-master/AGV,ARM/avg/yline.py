import cv2
import numpy as np
from pymycobot.myagv import MyAgv
import threading
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '172.30.1.27'
port = 1201
s.connect((host, port))

stream_url = 'http://172.30.1.27:8080/?action=stream'
cap = cv2.VideoCapture(stream_url)
#MA = MyAgv('/dev/ttyAMA2', 115200)


def process_frame(frame):
    height, width, _ = frame.shape
    roi_height = int(height / 3)
    roi_top = height - roi_height
    roi = frame[roi_top:, :]

    cv2.line(roi, (width // 2, 0), (width // 2, roi_height), (255, 0, 0), 2)
    
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    cv2.imshow("yellow_mask", yellow_mask) 

    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    direction = None
    if len(contours) >= 1:
        max_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)
        
        M = cv2.moments(max_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = roi_height // 2
            
            center_line = width // 2
            if cx < center_line - 50:
                direction = "LEFT" 
                s.sendall(b'L')

                # counterclockwise
                #MA.counterclockwise_rotation(40)
                #time.sleep(3)

            elif cx > center_line + 50:
                direction = "RIGHT"
                s.sendall(b'R')
                # clockwise
                #MA.clockwise_rotation(40)
                #time.sleep(3)

            else:
                direction = "FORWARD"
                s.sendall(b'F')
                # forward
                #MA.go_ahead(40)
                #time.sleep(3)
                
            # 화면에 화살표 그리기
            if direction == "LEFT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line - 50, roi_top + cy), (0, 0, 255), 5)
            elif direction == "RIGHT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line + 50, roi_top + cy), (0, 0, 255), 5)
            elif direction == "FORWARD":
                cv2.arrowedLine(frame, (center_line, roi_top + cy + 20), (center_line, roi_top + cy - 20), (0, 0, 255), 5)
                
    else:
        # 노랑색 라인이 감지되지 않을 때 STOP 표시
        direction = "STOP"
        s.sendall(b'S')
        cv2.putText(frame, "STOP", (width // 2 - 50, roi_top + roi_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #MA.stop()

    return direction

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break
    result = process_frame(frame)
    if result:
        print(result)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        s.close()
        break

cap.release()
cv2.destroyAllWindows()

# 메인 스레드에서 카메라 스레드 실행
#camera_thread = threading.Thread(target=camera_thread)
#camera_thread.start()

# 카메라 스레드가 종료될 때까지 대기
#camera_thread.join()