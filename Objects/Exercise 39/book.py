class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf:
    def __init__(self):
        self.books_on_shelf = []
        self.shelf_width = 100

    def add_books(self, *new_books):
        for book in new_books:
            if sum(book.width for book in self.books_on_shelf) + book.width > self.shelf_width:
                raise Exception('Sorry, not enough space for another book')
            self.books_on_shelf.append(book)

    def total_price(self):
        return sum(book.price for book in self.books_on_shelf)

    def has_book(self, checked_book):
        return checked_book in (book.title for book in self.books_on_shelf)

    def __repr__(self):
        return '\n'.join(book.title for book in self.books_on_shelf)


b1 = Book('Harry Potter', 'J.K. Rowling', 20, 30)
b2 = Book('Game of Throne', 'George R.R. Martin', 30, 30)
b3 = Book('Hyperion', 'Dan Simmons', 25, 30)
b4 = Book('Three-body problem', 'Cixin Liu', 40,30 )

my_book_shelf = Shelf()
my_book_shelf.add_books(b1, b2, b3)
print(my_book_shelf.total_price())
print(my_book_shelf.has_book('Harry Potter'))
print(my_book_shelf.has_book('Hunger games'))

my_book_shelf.add_books(b4)
print(my_book_shelf)


