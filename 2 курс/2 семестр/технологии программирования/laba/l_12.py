import time

class Book:
    book_id = 0

    def __init__(self, name = ''):
        Book.book_id += 1
        self.id = f'BOOK-{Book.book_id}'
        self.name = name

    def __str__(self):
        return f'Книга: {self.name}'

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class ReaderTicket:
    def __init__(self, owner_id = ''):
        self.owner_id = owner_id
        self.rented_books = []

    def __str__(self):
        return f'ID відвідувача: {self.owner_id}'

    def add_book(self, book = Book()):
        self.rented_books.append({
            'book_id': book.get_id(),
            'when_rented': time.ctime(time.time()),
            'should_returned': time.ctime(time.time() + 60 * 60 * 24 * 10)
        })
        print(f'запис у книжному білеті {self.rented_books}')

    def get_rented_books(self):
        return list(self.rented_books)

    def get_owner_id(self):
        return self.owner_id

class Reader:
    reader_id = 0

    def __init__(self, name= ''):
        Reader.reader_id += 1
        self.id = f'READER-{Reader.reader_id}'
        self.name = name
        self.reader_ticket = ReaderTicket(self.id)

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id

    def take_book(self, book = Book()):
        self.reader_ticket.add_book(book)

    def get_name(self):
        return self.name

    def get_reader_ticket(self):
        return self.reader_ticket


class Library:
    def __init__(self, name = '', books = [], rented_books = []):
        self.books = books
        self.allowed_books = list(books)
        self.rented_books = rented_books
        self.name = name

    def __str__(self):
        return f'Бібліотека {self.name} вітає вас'

    def create_request(self, reader = Reader(), book = Book()):
        if book in self.allowed_books:
            self.allowed_books.remove(book)
            reader.take_book(book)
            print('Гарного читання')
            return True
        print('Даної книги нажаль немає')
        return False

    def get_books(self):
        return list(self.books)

    def get_allowed_books(self):
        return list(self.allowed_books)

    def get_name(self):
        return self.name


# book_1 = Book('book 1')
book_2 = Book('book 2')
book_3 = Book('book 3')
book_4 = Book('book 4')
book_5 = Book('book 5')
book_6 = Book('book 6')
book_7 = Book('book 7')

print(book_1.get_id())
print(book_1.get_name())
print(book_1)

print(book_2.get_id())

reader_1 = Reader('reader 1')
reader_2 = Reader('reader 2')
reader_3 = Reader('reader 3')
reader_4 = Reader('reader 4')
reader_5 = Reader('reader 5')
reader_6 = Reader('reader 6')
reader_7 = Reader('reader 7')
reader_8 = Reader('reader 8')

print(reader_1.get_id())
print(reader_1.get_reader_ticket())
print(reader_1.get_name())
print(reader_1)

print(reader_2.get_id())

library = Library('library 1', [book_1, book_2, book_3, book_4, book_5, book_6, book_7])

print(library.get_name())
print(library.get_books())
print(library.get_allowed_books())
print(library)

library.create_request(reader_1, book_1)
library.create_request(reader_2, book_2)
library.create_request(reader_3, book_3)
library.create_request(reader_4, book_4)
library.create_request(reader_5, book_5)
library.create_request(reader_6, book_6)
library.create_request(reader_7, book_7)
library.create_request(reader_8, book_1)