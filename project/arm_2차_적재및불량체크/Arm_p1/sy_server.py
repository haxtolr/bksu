import asyncio
import aioconsole

HOST = '127.0.0.1'
PORT = 8889

ON_1 = False
ON_2 = True

async def handle_client(reader, writer):
    print("클라이언트가 연결되었습니다.")

    while True:
        try:
            data = await reader.read(100)
            message = data.decode()
            print('상대방:', message)
            msg = "ok"
            writer.write(msg.encode())

            #if message == "start":
            #    writer.write("start".encode())
            #    await writer.drain()
            #elif message == "end":
            #    writer.write("end".encode())
            #    await writer.drain()
            #    break
            #elif message == "work":
            #    writer.write("work_check".encode())
            #    await writer.drain()
            #elif message == "p":
            #    writer.write("p_check".encode())
            #    await writer.drain()
            #elif message == "g":
            #    writer.write("g_check".encode())
            #    await writer.drain()
            #elif message == "y":
            #    writer.write("y_check".encode())
            #    await writer.drain()
            #elif message == "o":
            #    writer.write("o_check".encode())
            #    await writer.drain()
            #elif message == "cho":
            #    input_msg = await aioconsole.ainput("메시지 입력: ") # 버릴 색상 입력
            #    writer.write(input_msg.encode())
            #    await writer.drain()
            #elif message == "pick_end":
            #    if ON_1 == True:
            #        writer.write("ON_1".encode())
            #        await writer.drain()
            #    elif ON_2 == True:
            #        writer.write("ON_2".encode())
            #        await writer.drain()
            #    else:
            #        writer.write("wait".encode())
            #        await writer.drain()
        except Exception as e:
            print(f"에러 발생: {e}")
            break

    print("Closing the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)

    print(f'Serving on {HOST}:{PORT}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
