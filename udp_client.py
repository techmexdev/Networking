from socket import *

server_name = 'localhost'
server_port = 3000

# create local UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    # get user input
    message = input(f'\nSend a letter to {server_name}:{server_port}\n')

    encoded_message = message.encode()
    client_socket.sendto(encoded_message, (server_name, server_port))

    # 4096 is reccomended buffer size: https://docs.python.org/3/library/socket.html#socket.socket.recv
    response, server_address = client_socket.recvfrom(4096)

    print(f'received letter from {server_address}:\n{response.decode()}')
