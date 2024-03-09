import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)

server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=5)

    if len(events) == 0:
        print("Событий нет!, Подождем еще!")

    for event, _ in events:
        event_socket: socket.socket = event.fileobj

        if event_socket == server_socket:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)

            print(f"Получен запрос на подключение от {client_address}!")

            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f"Получены данные: {data}!")
            event_socket.sendall(data)
