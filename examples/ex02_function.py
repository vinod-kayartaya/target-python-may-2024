"""
Example of a user defined function.
A function is a callable entity, that performs some actions.
A function can receive arguments (or aka parameters), and optionally
return a value
"""

# print(f'inside ex02_function.py, __name__ is {__name__}')

def is_even(num: int) -> bool:
    """
    This function returns True if the given number is disible by 2.
    Otherwise False is returned.
    """
    return num % 2 == 0


if __name__ == '__main__':
    n1 = int(input('Enter a number: '))
    result = 'even' if is_even(n1) else 'odd'

    print(f'The input number {n1} is an {result} number.')
