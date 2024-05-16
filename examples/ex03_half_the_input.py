"""
This script is supposed to accept a number,
if it is even, divide by 2 and print the result
if it is odd, add 1 and then divide by 2 and print the result 
"""

# print(f'inside ex03_half_the_input.py, __name__ is {__name__}')


from ex02_function import is_even
# import ex02_function

def main():
    n1 = int(input('Enter a number for finding the half: '))

    result = None
    if is_even(n1):
        result = n1/2
    else:
        result = (n1+1)/2

    print(f'{result = }')


if __name__ == '__main__':
    main()
