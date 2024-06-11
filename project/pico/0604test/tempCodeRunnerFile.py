
async def send_message():
    uri = "ws://localhost:8001/ws/control/"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Enter a message to send: ")
            await websocket.send(json.dumps({'message': message}))
            print("Message sent")