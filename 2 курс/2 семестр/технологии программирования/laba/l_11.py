from random import randint

class Book:
    def __init__(self, name, authors, publisher, year_of_publishing, page_count, price, paliturka_type):
        self._id = randint(1, 1000000)
        self._name = name
        self._authors = authors
        self._publisher = publisher
        self._year_of_publishing = year_of_publishing
        self._page_count = page_count
        self._price = price
        self._paliturka_type = paliturka_type

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getAuthors(self):
        if isinstance(self._authors, str):
            return self._authors
        return list.copy(self._authors)

    def getPublisher(self):
        return self._publisher

    def getYearOfPublishing(self):
        return self._year_of_publishing

    def getPageCount(self):
        return self._page_count

    def getPrice(self):
        return self._price

    def getPaliturkType(self):
        return self._paliturka_type


class BookShelf:
    def __init__(self, books = []):
        self.books = books

    def addBook(self, book):
        self.books.append(book)

    def getBooksNameByAuthorName(self, author_name):
        books_names = []
        for book in self.books:
            if author_name in book.getAuthors() or author_name == book.getAuthors():
                books_names.append(book.getName())
        return books_names

    def getBooksNameByPublisherName(self, publisher_name):
        books_names = []
        for book in self.books:
            if publisher_name == book.getPublisher():
                books_names.append(book.getName())
        return books_names

    def getBooksYearlierThanYear(self, year):
        books_names = []
        for book in self.books:
            if book.getYearOfPublishing() >= year:
                books_names.append(book.getName())
        return books_names

book1 = Book('Book1', 'Author1', 'Publisher1', 2000, 100, 50, '1')
book2 = Book('Book2', 'Author2', 'Publisher2', 2002, 102, 52, '2')
book3 = Book('Book3', 'Author3', 'Publisher3', 2003, 103, 53, '3')
book4 = Book('Book4', ['Author1'], 'Publisher1', 2004, 104, 54, '1')
book5 = Book('Book5', ['Author2'], 'Publisher2', 2005, 105, 55, '2')
book6 = Book('Book6', ['Author3'], 'Publisher3', 2006, 106, 56, '3')
book7 = Book('Book7', ['Author1', 'Author2'], 'Publisher1', 2007, 107, 57, '4')
book8 = Book('Book8', ['Author2', 'Author3'], 'Publisher2', 2008, 108, 58, '1')
book9 = Book('Book9', ['Author3', 'Author1'], 'Publisher3', 2009, 109, 59, '4')

book_shelf = BookShelf([book1, book2, book3, book4])

book_shelf.addBook(book5)
book_shelf.addBook(book6)
book_shelf.addBook(book7)
book_shelf.addBook(book8)
book_shelf.addBook(book9)

print('-' * 15)

print(book_shelf.getBooksNameByAuthorName('Author1'))
print(book_shelf.getBooksNameByAuthorName('Author2'))
print(book_shelf.getBooksNameByAuthorName('Author3'))

print('-' * 15)

print(book_shelf.getBooksNameByPublisherName('Publisher1'))
print(book_shelf.getBooksNameByPublisherName('Publisher2'))
print(book_shelf.getBooksNameByPublisherName('Publisher3'))

print('-' * 15)

print(book_shelf.getBooksYearlierThanYear(1990))
print(book_shelf.getBooksYearlierThanYear(2000))
print(book_shelf.getBooksYearlierThanYear(2005))