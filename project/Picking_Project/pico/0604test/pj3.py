import cv2
import numpy as np
import asyncio
import socket
import time
import threading
import websockets
import json

# 소켓 제작 및 서버 연결
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '172.30.1.87'
port = 2124
s.connect((host, port))
corossroad = False
done_command = None
count = 0
stop =False

def get_input():
    global done_command
    
    while True:
        done_command = input("Enter u: ")
        if done_command == "U" or done_command=="u":            #u 180도 : 빨간색을 만났을때
            break


order_receive=False
order_id = None

async def send_message(message):
    global order_id
    
    uri = "ws://172.30.1.81:8001/ws/control/"
    async with websockets.connect(uri) as websocket_connection:
    
        while True:
            await websocket_connection.send(json.dumps({'message': message}))
            print(f"Message sent:{message}")
            break

async def receive_messages():
    global order_id

    uri = "ws://172.30.1.81:8001/ws/control/"   
    while True:
        try:
            async with websockets.connect(uri) as websocket_connection:
                while True:
                    try:
                        message = await websocket_connection.recv()
                        data = json.loads(message)

                        # 'message' 키가 존재하는지 확인
                        if 'message' not in data:
                            print("Key 'message' not found in data")
                            continue

                        inner_message_data = data['message']

                        # 'message' 키가 inner_message_data에 존재하는지 확인
                        if 'message' not in inner_message_data:
                            print("Key 'message' not found in inner message data")
                            continue

                        message_value = inner_message_data['message']
                        print(message_value)

                        if '_' in message_value:
                            order_id = message_value.split('_')[0]
                            print(f"Order ID: {order_id}")
                            if message_value.split('_')[1] in ['a', 'b', 'c', 'd']:
                                return message_value.split('_')[1]
                        elif message_value in ['U', 'ok']:
                            return message_value
                        else:
                            pass
                    except json.JSONDecodeError as e:
                        print(f"JSON decode error: {e}")
                    except websockets.ConnectionClosed as e:
                        print(f"WebSocket connection closed: {e}")
                        await asyncio.sleep(5)
                        continue
                        
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        break  # 다른 예외가 발생하면 웹소켓 연결을 종료하고 재연결을 시도
        except websockets.ConnectionClosed as e:
            print(f"WebSocket connection failed to connect: {e}")
        except Exception as e:
            print(f"An error occurred while connecting: {e}")
        
        # 재연결을 시도하기 전에 잠시 대기
        print("Reconnecting in 5 seconds...")
        await asyncio.sleep(5)

# 데이터를 비동기로 받는 함수
async def receive_data():
    data = await asyncio.to_thread(s.recv, 1024)
    if not data:
        return None
    decoded_data = data.decode()
    print('받은 데이터 : ', decoded_data)
    return decoded_data

# 서버에 명령을 보내는 비동기 함수
async def send_command(command):
    
    global s,stop,count
    
    if stop:
        while True:
            done=await receive_data()
            if done == "done":
                print("done")
                stop = False
                count = count + 1
                print(count)
                break
    else:
        s.sendall(command.encode())
        await asyncio.sleep(0)  # 이벤트 루프의 다른 작업이 중단되지 않도록 함

# 빨간색을 인식하는 비동기 함수
async def process_frame_red(frame):
                
    global done_command ,initial_command
    global count,stop,order_id,order_receive
    
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
    # 빨간색 검출 
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.erode(red_mask, kernel, iterations=1)
    regions = cv2.bitwise_and(roi, roi, mask=combined_mask)
    blur = cv2.GaussianBlur(regions, (3, 3), 0)
    edges = cv2.Canny(blur, 50, 200)
    
    contours_red, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
     # 빨간색이 보이면 멈추는 코드        
    if len(contours_red) >= 1:
        max_contour_RED = max(contours_red, key=cv2.contourArea)  # 외각선 찾기
        cv2.drawContours(roi, [max_contour_RED], -1, (0, 255, 0), 2)
        # 빨간색으로 감지된 객체의 면적을 계산
        red_area = cv2.contourArea(max_contour_RED)
        # 면적이 일정 크기 이상이면 로봇을 멈춤
        if int(red_area) >= 1400: # 빨간 면적을 1500으로 잡음
            direction ="STOP"
            await send_command('S')
            if count ==2:
                await send_message(f"{order_id}_avg_arrived")
                done_command = await receive_messages()
                
            # U: 작업자가 물건을 받았을때 recieve, u: 도착지에 도착했을경우 send
            if done_command =="U" and count ==2:
                await send_command('RAR')
                time.sleep(0.5)
                done_command = None
                
               
                stop =True
               
                # return "rr"
                
            if count ==5:
                
                
                await send_message(f'{order_id}_avg_home')
                initial_command=None
                count = 0
                print(count)
                order_id=None
                done_command = None
                order_receive=False

                return "rr"
        else:
            direction = "GO"
    else:
        direction = "GO"
    return direction
   
# 프레임을 처리하는 비동기 함수
async def process_frame(frame):
    global corossroad
    global initial_command
    global count ,stop,order_id
    
    direction = None  # 변수 초기화

    height, width, _ = frame.shape
    roi_height = int(height / 3)
    roi_top = height - roi_height
    roi = frame[roi_top:, :]

    # ROI에 선을 그림
    #cv2.line(roi, (width // 5, 0), (width // 5, roi_height), (0, 0, 255), 2)  # 왼쪽
    cv2.line(roi, (width // 2, 0), (width // 2, roi_height), (255, 0, 0), 3)  # 중앙
    #cv2.line(roi, (width // 5 * 4, 0), (width // 5 * 4, roi_height), (0, 0, 255), 2)  # 오른쪽

    # 노란색 범위
    lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
    upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

    lower_darkblue = np.array([20,100, 100], dtype=np.uint8)
    upper_darkblue = np.array([30, 255, 255], dtype=np.uint8)
    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    darkblue_mask = cv2.inRange(hsv, lower_darkblue, upper_darkblue)
    
    combined_mask = cv2.bitwise_or(yellow_mask, darkblue_mask)
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.erode(combined_mask, kernel, iterations=1)
    regions = cv2.bitwise_and(roi, roi, mask=combined_mask)
  
    blur = cv2.GaussianBlur(regions, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 200)
    
    # 왼쪽, 중앙, 오른쪽에 노란색이 있는지 확인
    left_yellow = edges[:, :width // 8].any()
    right_yellow = edges[:, width // 8 * 7:].any()
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not stop and len(contours) >= 1:
        max_contour = max(contours, key=cv2.contourArea)
        _, _, w, _ = cv2.boundingRect(max_contour)  # Contour의 너비를 측정합니다.
        cv2.drawContours(roi, [max_contour], -1, (255, 0, 0), 2)
        M = cv2.moments(max_contour)
        #print(w * 0.5)
        #print(roi_height)
        # print(f"교차로인식 w는 {w *0.5} 그리고 로이는 {roi_height}")
        # print(f"left:{left_yellow} right:{right_yellow}")
        
        if not stop and w * 0.8 > roi_height and count == 0 and left_yellow and right_yellow: # Contour의 너비가 ROI의 1.5배보다 크면 교차로로 판단합니다.
            corossroad = True # 가로 넓이가 길때 W높일수록 인식못함
            # print(corossroad)
            # print(count)
            if initial_command == "a" or initial_command == "b":
                await send_command('HL')
                stop=True
                time.sleep(1)
                direction = "HL"
                await send_message(f"{order_id}_step_1")
                
            elif initial_command == "c" or initial_command == "d":
                await send_command('HR')
                stop=True
                time.sleep(1)
                direction = "HR"
                await send_message(f"{order_id}_step_1")
                
            elif initial_command == "h":
                await send_command('F')
                stop=True
                direction = "h"
                
        

        elif not stop and w  > roi_height and count == 1 and left_yellow and right_yellow: # Contour의 너비가 ROI의 1.5배보다 크면 교차로로 판단합니다.
            corossroad = True # 가로 넓이가 길때 W높일수록 인식못함
            # print(corossroad)
            # print(count)
            if initial_command =="a":
                await send_command('HL')
                direction = "HL"
                stop=True
                time.sleep(1)
                await send_message(f"{order_id}_step_2")
            elif initial_command=="b":

                await send_command('HR')
                direction = "HR"
                stop=True
                time.sleep(1)
                await send_message(f"{order_id}_step_2")


            elif initial_command=="c":

                await send_command('PL')
                direction = "PL"
                stop=True
                time.sleep(1)
                await send_message(f"{order_id}_step_2")
            elif initial_command=="d":

                await send_command('PR')
                direction = "PR"
                stop=True
                time.sleep(1)
                await send_message(f"{order_id}_step_2")
            
            elif initial_command == "h":
                await send_command('F') 
                direction = "h"
                stop=True

        elif not stop and w > roi_height and count == 3:
            #B와C의 입장
            if left_yellow and (initial_command=='b' or initial_command=='d'):
                await send_command('HL') 
                direction = "HL"
                stop=True
                time.sleep(1)
            elif right_yellow and (initial_command=='a' or initial_command=='c'):
                await send_command('HR') 
                direction = "HR"
                stop=True
                time.sleep(1)

        elif not stop and w > roi_height and count == 4:
            if left_yellow and (initial_command=='c' or initial_command=='d'):
                await send_command('HL') 
                direction = "HL"
                stop=True
                time.sleep(1)
            elif right_yellow and (initial_command=='a' or initial_command=='b'):
                await send_command('HR') 
                direction = "HR"
                stop=True
                time.sleep(1)


        elif M["m00"] != 0:
            corossroad = False
            #print(corossroad)
            cx = int(M["m10"] / M["m00"])
            cy = roi_height // 2
            center_line = width // 2
            if cx < center_line - 20:
                direction = "LEFT"
                await send_command('L')
                # if count ==3:
                #     print(f"stop: {stop},W:{w*1.5},count:{count}")
            elif cx > center_line + 20:
                direction = "RIGHT"
                await send_command('R')
                # if count ==3:
                #     print(f"stop: {stop},W:{w*1.5},count:{count}")
            # elif initial_command == "A" and left_yellow and right_yellow:
            #     direction = "PL"
            #     await send_command('PL')
            # elif initial_command == "B" and left_yellow and right_yellow:
            #     await send_command('PR')
            #     direction = "PR"
            else:
                direction = "FORWARD"
                await send_command('F')
                if count ==4:
                    print(f"stop: {stop},W:{w*1.5},count:{count}")
            if direction == "LEFT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line - 50, roi_top + cy), (255, 255, 255), 5)
            elif direction == "RIGHT":
                cv2.arrowedLine(frame, (center_line, roi_top + cy), (center_line + 50, roi_top + cy), (255, 255, 255), 5)
            elif direction == "FORWARD":
                cv2.arrowedLine(frame, (center_line, roi_top + cy + 20), (center_line, roi_top + cy - 20), (255, 255, 255), 5)

        # elif corossroad:
        #     if initial_command == "A":
        #         await send_command('PL')
        #         await send_command('F')
        #         direction = "PL"
        #     elif initial_command == "B":
        #         await send_command('PR')
        #         await send_command('F')
        #         direction = "PR"
        #     corossroad = False
    else:
        # if initial_command == "A":
        #     await send_command('L')
        # elif initial_command == "B":
        #     await send_command('R')
        await send_command('S')
        cv2.putText(frame, "STOP", (width // 2 - 50, roi_top + roi_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    await asyncio.sleep(0)  # 이벤트 루프의 다른 작업이 중단되지 않도록 함
    #print(direction)
    return direction

# 프레임 읽기를 비동기로 처리하는 함수
async def read_frame(cap):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera error")
            await asyncio.sleep(1)
            continue
        await asyncio.sleep(0)
        yield frame

initial_command = None
receive_command= None
# 메인 함수
async def main():
    global count ,receive_command,order_receive
    

    while True:
        global initial_command
            # 사용자의 초기 명령 입력
        if initial_command == "a" or initial_command == "b" or initial_command=="c" or initial_command=="d":
                pass
        else:
            initial_command = await receive_messages()
            if not order_receive:
                await send_command('or')
                print("or")
                order_receive=True
            print(initial_command)

        if stop:
            # 검은색 화면 생성
                black_frame = np.zeros_like(frame)
                await process_frame(black_frame)
                rr = await process_frame_red(black_frame)
                cv2.imshow("Frame", black_frame)
                await asyncio.sleep(1)  # 1초 동안 검은 화면 유지
                continue

        else:    
            stream_url = 'http://172.30.1.87:8080/?action=stream'
            cap = cv2.VideoCapture(stream_url)
        
            async for frame in read_frame(cap):
            # 프레임 처리
                await process_frame(frame)
                rr = await process_frame_red(frame)
            #print(result)
            # 프레임 출력
                cv2.imshow("Frame", frame)
                if rr == "rr" or cv2.waitKey(1) & 0xFF == ord('q') or stop:
                    print("화면 부팅.")
                    break
        
        cap.release()
        cv2.destroyAllWindows()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()    
# 메인 함수 실행
if __name__ == "__main__":
    asyncio.run(main())
