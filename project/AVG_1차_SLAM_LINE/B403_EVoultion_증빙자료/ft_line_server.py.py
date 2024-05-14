import socket
from pymycobot.myagv import MyAgv

#avg 인스턴스 선언
#포트와 시리얼
MA = MyAgv('/dev/ttyAMA2', 115200)

#클라이언트 처리함수
def handle_server(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            #클라이언트 데이터 수신부분(256바이트)
            data = conn.recv(256)
            if not data:
                break
            message = data.decode()
            #각 메시지를 받으면 출력해주고 좌, 우 전진 명령을 내림
            if message == 'end':
                print('End')
                break
            elif message == 'L':
                print('L')
                MA.counterclockwise_rotation(1, timeout=0.3)
            elif message == 'R':
                print('R')
                MA.clockwise_rotation(1, timeout=0.3)
            elif message == 'F':
                print('F')
                MA.go_ahead(1, timeout=0.5)
            elif message == 'STOP':
                print('Stop')
                MA.stop()
            else:
                print("none")

#메인
def main():
    # 호스트와 포트를 설정
    host = ''
    port = 9025
    # 소켓을 생성하고 바인드하고, 리스닝 상태로 변경
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f'Serving on {host}:{port}')

        #클라이언트를 계속해서 받음 (클로즈는 에러 때문에 안넣음, 넣어두댐)
        while True:
            conn, addr = s.accept()
            handle_server(conn, addr)

if __name__ == "__main__":
    main()
