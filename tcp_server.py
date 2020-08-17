from socket import *

server_port = 3000
# SOCK_STREAM = TCP. create welcoming socket
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('localhost' ,server_port))

# listen for TCP requests
server_socket.listen(1)

print(f'UDP server is ready at port {server_port}')

while True:
    # waits for tcp request, then creates new connection_socket
    connection_socket, client_address = server_socket.accept()
    
    message = connection_socket.recv(4096).decode()
    print(f'\nreceived message from {client_address}:\n{message}')

    reply = message.upper()
    print(f'sending message to {client_address}:\n{reply}')

    connection_socket.send(reply.encode())

    print(f'closed connection with {client_address}')

    # closes connection to client, but not welcoming socket.
    connection_socket.close()
