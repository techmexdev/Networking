from socket import *

server_port = 3000

# create UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# bind socket to local port
server_socket.bind(('localhost', server_port))

print(f'UDP server ready on port {server_port}... ')

while True:
    # read from UDP socket we just created
    # 4096 is reccomended buffer size: https://docs.python.org/3/library/socket.html#socket.socket.recv
    message, client_address = server_socket.recvfrom(4096)
    print(f'received message {message} from {client_address}')

    reply = message.decode().upper()

    print(f'sending message {reply} to {client_address}\n')
    server_socket.sendto(reply.encode(), client_address)
