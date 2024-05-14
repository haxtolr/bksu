import cv2
import numpy as np
import asyncio
import socket

# 소켓 제작 및 서버 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '172.30.1.64'
port = 9025
s.connect((host, port))

# 서버에 명령을 보내는 비동기 함수
async def send_command(command):
    global s
    s.sendall(command.encode())

# 프레임을 처리하는 비동기 함수
async def process_frame1(frame):
    height, width, _ = frame.shape #프레임의 높이, 너비
    roi_height = height  # roi 높이
    roi_top = height - roi_height # roi 시작점
    roi = frame[roi_top:, :] # roi 영역
    direction=None
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 빨간색 범위1
    lower_red = np.array([0, 100, 100], dtype=np.uint8)
    upper_red = np.array([10, 255, 255], dtype=np.uint8)
    red_mask1 = cv2.inRange(hsv, lower_red, upper_red)
	# 빨간색 범위2
    lower_red = np.array([160, 100, 100], dtype=np.uint8)
    upper_red = np.array([179, 255, 255], dtype=np.uint8)
    red_mask2 = cv2.inRange(hsv, lower_red, upper_red)
    # 빨간색 마스크 
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     # 빨간색이 보이면 멈추는 코드        
    if len(contours_red) >= 1:
        max_contour_RED = max(contours_red, key=cv2.contourArea)  # 외각선 찾기
        cv2.drawContours(roi, [max_contour_RED], -1, (0, 255, 0), 2)
        # 빨간색으로 감지된 객체의 면적을 계산
        red_area = cv2.contourArea(max_contour_RED)
        # 면적이 일정 크기 이상이면 로봇을 멈춤
        print(red_area)
        if int(red_area) >= 1500: # 빨간 면적을 1500으로 잡음
            direction ="STOP"
        else:
            direction = "GO"
    else:
        direction = "GO"
    return direction
   


# 프레임을 처리하는 비동기 함수
async def process_frame(frame):
    height, width, _ = frame.shape #프레임의 높이, 너비
    roi_height = int(height / 3) # roi 높이
    roi_top = height - roi_height # roi 시작점
    roi = frame[roi_top:, :] # roi 영역
    # roi에 선을 그림
    cv2.line(roi, (width // 2, 0), (width // 2, roi_height), (255, 0, 0), 2)
    # 노란색 범위
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	# 노란색 외곽선 찾기
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) >= 1: # 노란색 선이 하나 이상 감지되면
        max_contour = max(contours, key=cv2.contourArea) # 외각선 찾기
        cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2) # 외각선 그리기
        #외각선 중심점 찾기
        M = cv2.moments(max_contour)
        if M["m00"] != 0: # 외각선의 면적이 0이 아니면
            cx = int(M["m10"] / M["m00"])
            cy = roi_height // 2
            # 중심점이 화면 중앙보다 왼쪽에 있으면
            center_line = width // 2
            if cx < center_line - 80: # 좌회전
                direction = "LEFT" 
                await send_command('L')
                print('L')
            elif cx > center_line + 80: # 우회전
                direction = "RIGHT" 
                await send_command('R')
                print('R')
            else: # 직진
                direction = "FORWARD"
                await send_command('F')
                print('F')
            if direction == "LEFT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line - 50, roi_top + cy), (255, 255, 255), 5)
            elif direction == "RIGHT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line + 50, roi_top + cy), (255, 255, 255), 5)
            elif direction == "FORWARD":
                cv2.arrowedLine(frame, (center_line, roi_top + cy + 20), (center_line, roi_top + cy - 20), (255, 255, 255), 5)
    else:
        # 노란색 선이 감지되지 않으면 정지
        direction = "STOP"
        await send_command('S')
        cv2.putText(frame, "STOP", (width // 2 - 50, roi_top + roi_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    return direction

# 메인 함수
async def main():
    # 스트림 url    
    stream_url = 'http://172.30.1.64:8080/?action=stream'
    cap = cv2.VideoCapture(stream_url)
    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        if not ret:
            # 카메라 에러
            print("Camera error")
            break
        result1 = await process_frame1(frame) # 빨간색 처리
		# 빨간색이 감지되면 정지
        if result1 == "STOP":
            print(result1)
            await send_command('S')
        # 빨간색이 감지되지 않으면 방향 처리
        elif result1 =="GO":
            # 결과 출력
            result = await process_frame(frame)
            print(result)
		# 프레임 출력
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# 메인 함수 실행
if __name__ == "__main__":
    asyncio.run(main())