def fibo(limit = 100):
    print('start of fibo()')
    a, b = -1, 1
    for _ in range(limit):
        c = a + b
        yield c
        a, b = b, c
    


def main():
    print(f'type of fibo is {type(fibo)}')
    f = fibo(10)
    print(f'type of f is {type(f)}')
    for i in f:  # same as i = next(f) in a loop, until the generator is done with
        print(i)



if __name__ == '__main__':
    main()

