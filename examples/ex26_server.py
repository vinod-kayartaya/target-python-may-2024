from socket import socket, AF_INET, SOCK_STREAM
import json
from threading import Thread


def handle_client(client_sock):
    request_message = (client_sock.recv(1024))
    print(request_message)
    request_message = request_message.decode('utf-8')
    print(request_message)
    request = json.loads(request_message)

    response = {}
    if request['method_name'] == 'factorial':
        try:
            result = factorial(request['method_args'][0])
            response['result'] = result
        except ValueError:
            response['error'] = 'Factorial of negative numbers not calculated here'
    elif request['method_name'] == 'fibonacci':
        response['error'] = 'functionality not ready yet'
    elif request['method_name'] == 'power':
        response['error'] = 'functionality not ready yet'
    else:
        response['error'] = 'Invalid method requested'

    resp_message = json.dumps(response).encode('utf-8')
    client_sock.send(resp_message)
    client_sock.close()


def factorial(num):
    if num < 0:
        raise ValueError()
    f = 1
    while num > 1:
        f *= num
        num -= 1

    return f


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.138.17', 2233)
    server_socket.bind(server_addr)
    server_socket.listen(5)
    print(f'server listening on port {server_addr[1]}')

    while True:
        print('waiting for a client connection...')
        client_sock, client_addr = server_socket.accept()
        print(f'got a client connection from {client_addr}')

        Thread(target=handle_client, args=(client_sock,)).start()






if __name__ == '__main__':
    main()

