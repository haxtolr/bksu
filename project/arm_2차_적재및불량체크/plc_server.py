import socket

# 서버의 IP 주소와 포트 번호
HOST = 'localhost'
PORT = 8081

# 소켓 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다. 클라이언트를 기다리는 중...')

    conn, addr = s.accept()
    ON_1 = False
    ON_2 = True
    with conn:
        print('연결됨:', addr)
        while True:
            data = conn.recv(1024)
            print('상대방:', data.decode()) 
            if data.decode() == "start": # 모든 작업 시작
                message = "시작"
                conn.sendall(message.encode())
            elif data.decode() == "end": # 모든 작업 종료
                message = "end"
                conn.sendall(message.encode())
                break
            elif data.decode() == "work": #로봇팔 작업중
                message = "work_check"
                conn.sendall(message.encode())
            elif data.decode() == "p": # 보라색 탐지 
                message = "p_check" # 보라색 탐지 확인
                conn.sendall(message.encode())
            elif data.decode() == "g": # 초록색 탐지
                message = "g_check" # 초록색 탐지 확인
                conn.sendall(message.encode())
            elif data.decode() == "y": # 노란색 탐지
                message = "y_check"  # 노란색 탐지 확인
                conn.sendall(message.encode())
            elif data.decode() == "o": # 주황색 탐지
                message = "o_check" # 주황색 탐지 확인
                conn.sendall(message.encode())
            elif data.decode() == "non": # 버릴 색상
                input_msg = input("메시지 입력: ") # 버릴 색상 입력
                conn.sendall(input_msg.encode())
            elif data.decode() == "pick_end": # 로봇팔이 물체 탐지하러 올는동안 물건이 레일 어디까지 왔는대 2초마다 물으면 대답하면 될듯?
                if ON_1 == True:
                    message = "ON_1"
                    conn.sendall(message.encode())
                elif ON_2 == True:
                    message = "ON_2"
                    conn.sendall(message.encode())
                else:
                    message = "wait"
                    conn.sendall(message.encode())
    s.close()
