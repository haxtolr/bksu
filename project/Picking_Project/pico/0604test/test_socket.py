import asyncio
import websockets
import json

async def send_message():
    uri = "ws://localhost:8001/ws/control/"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(json.dumps({'message': message}))
            print("Message sent")

async def receive_messages():
    uri = "ws://localhost:8001/ws/control/"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Message from server: {message}")

async def main():
    # 메시지를 보내는 작업과 메시지를 받는 작업을 비동기적으로 실행합니다
    await asyncio.gather(
        send_message(),
        receive_messages()
    )
if __name__ == "__main__":
    asyncio.run(main())