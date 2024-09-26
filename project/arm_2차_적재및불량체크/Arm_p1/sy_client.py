import asyncio

msg = "WAIT"

async def tcp_client(message):
    while True:
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 8888)

        print(f'보낸 메시지: {message!r}')
        writer.write(message.encode())

        data = await reader.read(100)
        print(f'받은 메시지: {data.decode()!r}')

        if message == "end":
            print("모든 작업을 종료합니다.")
            break

    print('연결 종료')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_client(msg))
