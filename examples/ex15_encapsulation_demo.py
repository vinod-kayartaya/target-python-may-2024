class Book:
    def __init__(self, **kwargs) -> None:
        self.__title = kwargs.get('title')
        self.__price = kwargs.get('price')
        self.__author = kwargs.get('author')

    def __str__(self) -> str:
        title = f'"{self.__title}"' if self.__title is not None else None
        author = f'"{self.__author}"' if self.__author is not None else None
        return f'Book(title={title}, price={self.__price}, author={author})'


def main():
    b1 = Book(title='Let us C', price=599, author='Y Kanitkar')
    print(b1)


if __name__ == '__main__':
    main()

