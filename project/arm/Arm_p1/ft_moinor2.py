import cv2
import numpy as np
import queue

cap = cv2.VideoCapture(0)

msg_send = "none"

def color_detect(frame):
    global msg_send
    # BGR에서 HSV로 색상 공간 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 초록색 범위
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    # 노랑색 범위
    lower_yellow = np.array([20, 100, 100])
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
    # 영역이 500 이상인 외곽선만 선택
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) >= 500]
    # 가장 큰 외곽선 찾기
    max_contour = max(large_contours, key=cv2.contourArea, default=None)
    if max_contour is not None:
        rect = cv2.minAreaRect(max_contour)
        box = cv2.boxPoints(rect)
        box = np.intp(box)
        # 사각형의 너비와 높이를 계산합니다.
        w, h = rect[1]
        if w == 0 or h == 0:
            ratio = 10
        if w != 0 and h != 0:
            ratio = w / float(h)
        if 0.4 < ratio < 1.3:
            # 각 색상별로 마스크를 적용하고, 결과 영상에서 픽셀 수를 세어 가장 큰 영역을 가진 색상을 찾기.
            masks = [("green", green_mask), ("yellow", yellow_mask), ("orange", orange_mask), ("purple", purple_mask)]
            max_color = max(masks, key=lambda x: cv2.countNonZero(x[1]))
            result = max_color[0]
        else:
            result = "NG"
            msg_send = "NG"
        
        return result, box
    else:
        return "NG", None
    


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

    # 
    color, box = color_detect(cropped_frame)
    if box is not None:
        cv2.rectangle(cropped_frame, tuple(box[0]), tuple(box[2]), (0, 255, 0), 2)
    cv2.putText(cropped_frame, color, (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 7)
    cv2.imshow('monitor', cropped_frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()