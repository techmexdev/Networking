from socket import *

server_name = 'localhost'
server_port = 3000

# SOCK_STREAM = TCP

while True:
    client_socket = socket(AF_INET, SOCK_STREAM)

    # connection must be established before sending data
    client_socket.connect((server_name, server_port))

    message = input(f'\nSend letter to {server_name}:{server_port}\n')
    encoded_message = message.encode()
    client_socket.send(encoded_message)

    # 4096 is reccomended buffer size: https://docs.python.org/3/library/socket.html#socket.socket.recv
    reply = client_socket.recv(4096)
    print(f'received letter from {server_name}:{server_port}:\n{reply.decode()}')
    client_socket.close()
