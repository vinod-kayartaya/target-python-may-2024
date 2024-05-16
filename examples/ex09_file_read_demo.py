FILENAME = './ex01_console_io.py'


def file_read_method1():
    file = None
    
    try:
        file = open(FILENAME)
        content = file.read()
        print(content)
    except Exception as err:
        print('Something went wrong!')
        print(err)
    finally:   
        if file is not None and not file.closed:
            print('closing the file...')
            file.close()


def file_read_method2():
    # context manager; automatically closes the resource in question
    with open(FILENAME) as file:  #  file = open(FILENAME)
        line_num = 1
        while True:
            line = file.readline()
            if line == '': 
                break
            print(f'{line_num:<4}: {line}', end='')
            line_num += 1
        # here file.close() is going to be called


def file_read_method3():
    # context manager; automatically closes the resource in question
    with open(FILENAME) as file:  #  file = open(FILENAME)
        line_num = 1
        for line in file:
            print(f'{line_num:<4}: {line}', end='')
            line_num += 1
        # here file.close() is going to be called


def main():
    file_read_method3()
    print()

if __name__ == '__main__':
    main()

