import socket

server_ip = input("input ip: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, 1706))
data = client_socket.recv(1024).decode()
print({data})
client_socket.close()