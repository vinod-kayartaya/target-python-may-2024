class Book:
    """
    class Book
    Reprents all the data and behaviours of a book object
    """
    
    def __init__(self):
        # self is the reference of the newly constructed object, passed by Python RT
        print(f'Book.__init__() called with self as {self}')
        self.title = 'let us c'
        self.price = 599
        self.author = 'Y Kanitkar'


def main():
    b1 = Book()
    b1.publisher = 'BPB Publication'
    b1.price = -888

    print(f'b1 is {b1}')
    print(f'attributes in b1 are: {dir(b1)}')
    print(f'type(b1) is {type(b1)}')
    print(f'type(Book) is {type(Book)}')


if __name__ == '__main__':
    main()

