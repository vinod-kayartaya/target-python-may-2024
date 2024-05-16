class Book:
    def __init__(self, **kwargs) -> None:
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        self.__author = kwargs.get('author')

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if value is not None and type(value) != str:
            raise TypeError('value must be a str')
        
        self.__title = value

    @property
    def price(this):
        return this.__price
    
    @price.setter
    def price(this, value):
        if value is not None and type(value) not in (int, float):
            raise TypeError('value must be a number')
        
        if value is not None and value < 0:
            raise ValueError('value must be >= 0')
        
        this.__price = value

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, value):
        if value is not None and type(value) != str:
            raise TypeError('value must be a str')
        
        self.__author = value

    def __str__(self) -> str:
        title = f'"{self.__title}"' if self.__title is not None else None
        author = f'"{self.__author}"' if self.__author is not None else None
        return f'Book(title={title}, price={self.__price}, author={author})'
    
    def print(self):
        print(f'Title   : {self.__title}')
        print(f'Price   : {self.__price}')
        print(f'Author  : {self.__author}')
        print()


def main():
    b1 = Book(title='Let us C', price=599, author='Y Kanitkar')
    print(b1)
    b1.print()  # b1 is implicitly passed as the first arg, and received into `self`
    Book.print(b1)  # print here is treated as a global function under the namespace called `Book`
    b2 = Book()
    # set functions are called here
    b2.title = 'Java Unleashed'  # b2.title('Java Unleashed')
    b2.author = 'John Doe'
    b2.price = 3500

    # get functions are called here
    print(f'{b2.title} is priced at Rs.{b2.price} and written by {b2.author}')

if __name__ == '__main__':
    main()

