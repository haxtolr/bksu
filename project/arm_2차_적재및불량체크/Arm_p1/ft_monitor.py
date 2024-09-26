import cv2
import numpy as np
import aioconsole
import asyncio
import threading
import socket

# 서버의 IP 주소와 포트 번호
HOST = '127.0.0.1'
PORT = 8888

ft_status = None
color = None
msg = None
re_msg = None
# 메시지
con_msg = "연결 성공"
start_msg = "start"
end_msg = "end"
work_msg = "work"
p_msg = "p"
g_msg = "g"
y_msg = "y"
o_msg = "o"

cap = cv2.VideoCapture(0)

def process_message(re_msg):
    color_dict = {
        'p': "Purple",
        'o': "Orange",
        'y': "Yellow",
        'g': "Green"
    }

    if re_msg is not None:
        exclude_colors = [color_dict[char] for char in re_msg if char in color_dict]
    else:
        exclude_colors = []

    color_ranges = [
        ("Green", [40, 100, 100], [80, 255, 255]),
        ("Yellow", [20, 150, 150], [30, 255, 255]),
        ("Orange", [5, 100, 100], [15, 255, 255]),
        ("Purple", [130, 50, 50], [170, 255, 255])
    ]

    color_ranges = [color for color in color_ranges if color[0] not in exclude_colors]

    return color_ranges

async def ft_color(frame):
    global color
    global msg
    text_x, text_y = 10, 30 # 텍스트를 표시할 위치
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 각 색상 범위 정의
    color_ranges = process_message(msg)

    for (color, lower, upper) in color_ranges:
        lower = np.array(lower)
        upper = np.array(upper)
        masks = cv2.inRange(hsv, lower, upper)

    # 각 색상 범위에 대한 마스크를 적용.
    masks = [cv2.inRange(hsv, np.array(lower), np.array(upper)) for (_, lower, upper) in color_ranges]
    total_mask = cv2.bitwise_or(*masks)

    # 마스크를 적용한 이미지에서 컨투어를 찾기.
    contours, _ = cv2.findContours(total_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        cv2.putText(frame, "NG", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        status = "NG"
        return
    for contour in contours:
        
        # 가장 큰 영역을 가진 컨투어만을 처리
        contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(contour)
        if area >= 500:
            # 컨투어를 감싸는 사각형을 계산.
            x, y, w, h = cv2.boundingRect(contour)

            # 사각형의 비율을 계산
            ratio = w / float(h)

            # 사각형을 그립니다.
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # 비율이 1:2 또는 2:1을 넘거나, 컨투어가 합친 마스크 내에 없는 경우 불량으로 판단
            if ratio > 2.0 or ratio < 0.5 or cv2.countNonZero(total_mask[y:y+h, x:x+w]) == 0:
                status = "NG"
                await ft_client(msg="NG")
            else:
                status = "OK"
                await ft_client(msg="OK")
                
            # 해당 색상의 이름을 찾기.
            for color_name, lower, upper in color_ranges:
                if cv2.inRange(hsv[y:y+h, x:x+w], np.array(lower), np.array(upper)).any():
                    color = color_name
                    await ft_client(msg=color)
                    break

            if status == "OK":
                cv2.putText(frame, f"{color}, : {status}", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            else:
                cv2.putText(frame, f"{color}, : {status}", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

async def ft_client(msg):
    global re_msg
    # 서버에 연결
    reader, writer = await asyncio.open_connection(HOST, PORT)

    # 메시지 전송
    writer.write(msg.encode())
    await writer.drain()

    # 서버로부터 응답 받기
    data = await reader.read(1024)
    if data:
        re_msg = repr(data.decode())
        print('Received : ', re_msg)

    # 소켓 닫기
    writer.close()
    await writer.wait_closed()


async def main():
    global msg
    global ft_status
    
    # ft_client()를 비동기 작업으로 실행.
    # 서버와의 통신을 담당.

    msg = "start"
    while True:
        # 프레임을 읽기.
        ret, frame = cap.read()
        # 색상을 구분하고 화면에 표시

        if msg == "start":
            await ft_client(msg="cho")
            await ft_color(frame)
        # 결과를 화면에 표시
        cv2.imshow('Webcam Monitoring', frame)

        # 종료.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            msg = "end"
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    asyncio.run(main())