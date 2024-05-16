"""
console-io

This is an example of accepting user inputs, perofming some actions and printing the result
"""

num1 = input('Enter a number: ')
n2 = input('Enter another number: ')

num1 = int(num1)  # here int() is a constructor call
n2 = int(n2)

print('n1 + n2 =', num1 + n2)
print(f'{num1 + n2 = }')
