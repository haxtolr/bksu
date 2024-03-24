import socket

class simple_server:
    def __init__(self):
        self.bufsize = 1024
        self.counter = 0

    def run(self,ip,port):
        #소켓 생성
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #소켓에 ip와 포트 정보를 bind
        self.sock.bind((ip,port))

        #소켓을 listen 상태로 전환, 정수는 대기 큐의 길이를 정의
        self.sock.listen(5)

        while self.counter < 5:    
            #client가 serv_sock로 request를 줄 때까지 process를 멈춤, client로부터 request가 오면 client와 통신하기 위한 clnt_sock를 생성
            clnt_sock,req_addr = self.sock.accept()

            #clnt_sock에 적힌 정보를 read
            req_message = clnt_sock.recv(self.bufsize)

            print("this is request message")
            print(req_message)

            res_message = '''HTTP/1.1 200 OK
Server:simple web server
Content-length:2048
Content-type:text/html

<html><head><title>simple web server</title></head>
<body>bye bye</body>
</html>

'''.encode("utf-8")

            print("this is response message")
            print(res_message)

            #clnt_sock를 통해서 client에 정보를 전송
            clnt_sock.send(res_message)

            #clnt_sock를 close
            clnt_sock.close()
            self.counter += 1

        #sock를 close
        print('close sock')
        self.sock.close()


server = simple_server()
server.run("127.0.0.1",8888)