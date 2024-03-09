import asyncio
import socket
import loguru

from types import TracebackType
from typing import Optional, Type

loguru.logger.add("server.log", format="{time} {level} {message}", level="DEBUG")


class ConnectedSocket:
    def __init__(self, server_socket: socket):
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        loguru.logger.info("Вход в контекстный менеджер, ожидание подключения")
        loop = asyncio.get_running_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        loguru.logger.info(f"Подключение от {address}")
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]) -> None:
        loguru.logger.info("Выход из контекстного менеджера")
        self._connection.close()
        loguru.logger.info("Соединение закрыто")


async def main():
    loop = asyncio.get_running_loop()

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)

    server_socket.bind(server_address)
    server_socket.listen()

    async with ConnectedSocket(server_socket) as connection:
        data = await loop.sock_recv(connection, 1024)
        loguru.logger.info(f"Получены данные: {data}")
        await loop.sock_sendall(connection, data)


asyncio.run(main())
