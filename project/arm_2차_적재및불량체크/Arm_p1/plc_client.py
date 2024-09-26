import socket

# 서버의 IP 주소와 포트 번호
HOST = '127.0.0.1'
PORT = 8883

# 메시지
con_msg = "연결 성공"
start_msg = "start"
end_msg = "end"
work_msg = "work"
p_msg = "p"
g_msg = "g"
y_msg = "y"
o_msg = "o"

# 소켓 객체 생성
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 서버에 연결
    s.connect((HOST, PORT))
    s.sendall(con_msg.encode())
    # 서버에 메시지 전송
    while True:
        # arm  pc에서 plc pc로 메시지 전송
        input_data = input("메시지 입력: ")
        if input_data == "end":
            s.sendall(end_msg.encode())
            break
        elif input_data == "pick_end":
            s.sendall("pick_end".encode())
        elif input_data == "start":
            s.sendall(start_msg.encode())
        elif input_data == "work":
            s.sendall(work_msg.encode())
        
        # 암에서 색을 판단해 보내줌
        elif input_data == "p": 
            s.sendall(p_msg.encode())
        elif input_data == "g":
            s.sendall(g_msg.encode())
        elif input_data == "y":
            s.sendall(y_msg.encode())
        elif input_data == "o":
            s.sendall(o_msg.encode())
        
        elif input_data == "non": # 버릴 색상
            s.sendall(input_data.encode())

        # 서버로부터 응답 받기
        data = s.recv(1024)
        if not data:
            continue
        print('받은 데이터 : ', repr(data.decode()))

        if repr(data.decode()) == "'end'":
            print("모든 작업을 종료합니다.")
            break
        elif repr(data.decode()) == "'o'":
            print("주황색이 선택되었습니다.")
        elif repr(data.decode()) == "'p'":
            print("보라색이 선택되었습니다.")
        elif repr(data.decode()) == "'g'":
            print("초록색이 선택되었습니다.")
        elif repr(data.decode()) == "'y'":
            print("노란색이 선택되었습니다.")
        elif repr(data.decode()) == "'ON_2'":
            print("물건이 라인에 도착했습니다.")
        elif repr(data.decode()) == "'ON_1'":
            print("물건이 라인에 올라왔습니다..")
        elif repr(data.decode()) == "'wait'":
            print("물건이 아직 도착하지 않았습니다. 대기 중입니다.")
