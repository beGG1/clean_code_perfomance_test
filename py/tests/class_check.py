import time

# Single large class implementation
class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.borrowed_books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = title

    def add_user(self, user_id, name):
        self.users[user_id] = name

    def borrow_book(self, user_id, book_id):
        if book_id in self.books and user_id in self.users:
            if book_id not in self.borrowed_books:
                self.borrowed_books[book_id] = user_id

    def return_book(self, user_id, book_id):
        if book_id in self.borrowed_books and self.borrowed_books[book_id] == user_id:
            del self.borrowed_books[book_id]

    def show_books(self):
        pass

    def show_users(self):
        pass

# Multiple smaller classes implementation
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_borrowed = False

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.borrowed_books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = Book(book_id, title)

    def add_user(self, user_id, name):
        self.users[user_id] = User(user_id, name)

    def borrow_book(self, user_id, book_id):
        if book_id in self.books and user_id in self.users:
            book = self.books[book_id]
            if not book.is_borrowed:
                book.is_borrowed = True
                self.borrowed_books[book_id] = user_id

    def return_book(self, user_id, book_id):
        if book_id in self.borrowed_books and self.borrowed_books[book_id] == user_id:
            book = self.books[book_id]
            book.is_borrowed = False
            del self.borrowed_books[book_id]

    def show_books(self):
        pass

    def show_users(self):
        pass

def measure_performance(library):
    # Add a large number of books and users
    for book_id in range(1, 1001):
        library.add_book(book_id, f"Book {book_id}")
    
    for user_id in range(1, 501):
        library.add_user(user_id, f"User {user_id}")

    # Perform borrow and return operations multiple times
    for _ in range(10):
        for user_id in range(1, 501):
            for book_id in range(1, 1001):
                library.borrow_book(user_id, book_id)
                library.return_book(user_id, book_id)

if __name__ == "__main__":
    # Measure performance of the single large class implementation
    library_system = LibrarySystem()
    start_time = time.time()
    measure_performance(library_system)
    print(f"Single large class implementation execution time: {time.time() - start_time:.6f} seconds")

    # Measure performance of the multiple smaller classes implementation
    library = Library()
    start_time = time.time()
    measure_performance(library)
    print(f"Multiple smaller classes implementation execution time: {time.time() - start_time:.6f} seconds")