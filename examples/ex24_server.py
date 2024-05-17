from socket import socket, AF_INET, SOCK_STREAM


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.138.17', 1234)
    server_socket.bind(server_addr)
    server_socket.listen(5)
    print(f'server listening on port {server_addr[1]}')

    while True:
        print('waiting for a client connection...')
        client_sock, client_addr = server_socket.accept()
        print(f'got a client connection from {client_addr}')
        username = client_sock.recv(1024)
        username = username.decode('utf-8')
        print(f'client name is {username}')

        message = f'Hello {username}. How are you?'
        client_sock.send(message.encode('utf-8'))


if __name__ == '__main__':
    main()

