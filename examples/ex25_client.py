from socket import socket, AF_INET, SOCK_STREAM


if __name__ == '__main__':
    print('client program started')
    server_addr = ('192.168.138.17', 1234)

    server = socket(AF_INET, SOCK_STREAM)
    server.connect(server_addr)
    print(f'connected to the server {server_addr}')
    username = input('enter your name: ')
    server.send(username.encode('utf-8'))
    message = server.recv(1024).decode('utf-8')
    print(f'server says - {message}')
    print('client program terminated')
