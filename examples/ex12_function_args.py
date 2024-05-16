def say_hello(name='friend', city='your city'):  # positional parameters (can receive keyword args also)
    print(f'hello {name}, how\'s weather in {city}?')

def greet(name, city, /):  # positional-only parameters (not supported in 3.7)
    print(f'hello {name}, how\'s weather in {city}?')

def sub_total(kind, *nums): # `kind` is a positional argument; nums is an arbitrary argument
    # `nums` is a tuple
    nums = [n for n in nums if type(n) in (int, float)]
    if kind==1: return sum(nums) / len(nums)  # avg
    if kind==2: return sum(nums)  # sum
    if kind==3: return max(nums)
    if kind==4: return min(nums)
    raise Exception('Unknown kind for the operation')


def print_book_details(**book):  # keyword arguments --> dict
    title = book.get('title', 'Unknown')
    price = book.get('price', 0.0)
    author = book.get('author', 'Unknown')

    print('The book details are:')
    print(f'Title  = {title}')
    print(f'Price  = {price}')
    print(f'Aithor = {author}')
    print('-'*50)


def main():
    print_book_details(title='Let us C', price=599.0, author='Y Kanitkar')
    print_book_details(title='Let us Python')
    print_book_details(title='Let us Flask', author='Vinod', publisher='ACME publication')

    data = {'title': 'Java Unleashed', 'price': 2999}
    print_book_details(**data)

    # say_hello('Vinod', 'Bangalore')
    # say_hello(city='Mumbai', name='Rahul')
    # say_hello('John')
    # say_hello()
    # say_hello(city='Dallas')

    # greet('Vinod', 'Bangalore')
    # # greet(city='Mumbai', name='Rahul')

    t = sub_total(2, 100, 200, 'vinod', 'kumar', 300)
    print(f't is {t}')
    nums = [1, 2, 3, 4, 5, 6]
    t = sub_total(2, *nums)
    print(f't is {t}')



if __name__ == '__main__':
    main()

