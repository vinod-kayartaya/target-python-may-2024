def factorial(num: int) -> int:
    if type(num) != int:
        raise TypeError(f'expecting class <int>, but got {type(num)}')

    if num <= 1:
        return 1

    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f


def print_table(num: int) -> None:
    if type(num) != int:
        print(f'Can\'t print table for this - {num}')
        return
    
    for i in range(1, 21):
        print(f'{num} X {i} = {num*i}')


def dir2(obj):
    return [each_attr for each_attr in dir(obj) if not each_attr.startswith('_')]


def is_float(s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False
    

def csv2json(filename: str) -> None:
    to_list = lambda line : [int(value) if value.isnumeric() else value for value in line.strip().split(',')]
    try:
        with open(filename) as file:
            fields = file.readline().strip().split(',')
            customers = [ dict(zip(fields, to_list(line))) for line in file]
            
        import json  # not a good practice; but doable
        from time import time
        out_filename = f'{filename[:-4]}-{time()}.json'
        with open(out_filename, 'wt') as out_file:
            json.dump(customers, out_file, indent=4)
            print(f'{filename} is now converted to JSON and stored in{out_filename}')


    except OSError as err:
        print(err)

