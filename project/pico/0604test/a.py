import asyncio
import websockets
import json
from pymycobot import MyCobot
class WebSocketClient:
    def __init__(self):
        self.result = []  # 메시지를 저장할 배열

    async def receive_and_print_messages(self):
        url = 'ws://localhost:8001/ws/control/'
        try:
            async with websockets.connect(url) as websocket:
                start_time = asyncio.get_event_loop().time()  # 현재 시간 기록
                received_messages = False  # 메시지를 받았는지 여부
                while True:
                    try:
                        # 현재 시간부터 2초 동안 메시지를 기다립니다.
                        message = await asyncio.wait_for(websocket.recv(), timeout=2)
                        data = json.loads(message)  # 받은 메시지를 JSON으로 변환
                        if 'order' in data:
                            # 'order'가 있는 경우에만 처리
                            order_id = data['order']['id']
                            products = data['order']['products']
                            for product in products:
                                location = product['location']
                                quantity = product['quantity']
                                result_info = {'id': order_id, 'location': location, 'quantity': quantity}
                                self.result.append(result_info)  # 결과 저장
                        else:
                            print("Received message:", data)
                        self.print_and_reset_result()  # 결과 출력 및 초기화
                        received_messages = True  # 메시지를 받음
                    except asyncio.TimeoutError:
                        # 메시지를 받지 못한 경우
                        if received_messages:
                            break  # 이미 메시지를 받았으면 루프 종료
                        else:
                            pass
        except Exception as e:
            print("An error occurred while receiving messages:", e)

    def print_and_reset_result(self):
        print(self.result)  # 결과 출력
        self.result = []  # 결과 초기화

async def main():
    client = WebSocketClient()
    await client.receive_and_print_messages()

if __name__ == "__main__":
    asyncio.run(main())
