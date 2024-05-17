import json
from socket import socket, AF_INET, SOCK_STREAM


def menu():
    print("""
    ** Main menu **
    0. Exit
    1. Factorial 
    2. Fibonacci
    3. Power""")

    return int(input('Enter your choice: '))


def main():

    while True:
        choice = menu()
        if choice == 0:
            break

        if choice < 1 or choice > 3:
            print('Invalid choice. Please try again.')
            continue

        request = dict()
        if choice == 1:
            request['method_name'] = 'factorial'
            num = int(input('Enter a number: '))
            request['method_args'] = (num, )
        elif choice == 2:
            request['method_name'] = 'fibonacci'
            num = int(input('Enter a number: '))
            request['method_args'] = (num,)
        else:
            request['method_name'] = 'power'
            a = int(input('Enter value for `a`: '))
            b = int(input('Enter value for `b`: '))
            request['method_args'] = (a, b)

        message = json.dumps(request).encode('utf-8')
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(('192.168.138.17', 2233))
        server.send(message)
        resp_message = server.recv(1024)
        resp_message.decode('utf-8')
        response = json.loads(resp_message)
        server.close()

        if 'error' in response:
            print(f'There was an error: {response["error"]}')
        else:
            print(f'The result for {request["method_name"]} operation is {response["result"]}')

        print('-'*50)


if __name__ == '__main__':
    main()
