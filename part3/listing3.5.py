import asyncio
import socket
import loguru

from asyncio import AbstractEventLoop

loguru.logger.add("server.log", format="{time} {level} {message}", level="DEBUG")


async def echo(connection: socket, loop: AbstractEventLoop):
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b'boom\r\n':
                raise Exception("Неожиданная ошибка сети")
            await loop.sock_sendall(connection, data)
    except Exception as e:
        loguru.logger.error(f"Ошибка: {e}")
    finally:
        connection.close()


async def listen_for_connections(server_socket: socket.socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}!")
        await asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())


asyncio.run(main())
