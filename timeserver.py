import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.56.104', 1303))
server_socket.listen(1)
print("server start")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by client address:: {client_address}")

    current_time = datetime.now().strftime('%d.%m.%Y %H:%M') 
    client_socket.sendall(current_time.encode())

    client_socket.close()
    print(f"send: {current_time}")
