#include <iostream>
#include <unordered_map>
#include <string>
#include <chrono>

using namespace std;

// Single large class implementation
class LibrarySystem {
public:
    void addBook(int bookId, const string &title) {
        books[bookId] = title;
    }

    void addUser(int userId, const string &name) {
        users[userId] = name;
    }

    void borrowBook(int userId, int bookId) {
        if (books.count(bookId) && users.count(userId)) {
            if (!borrowedBooks.count(bookId)) {
                borrowedBooks[bookId] = userId;
            }
        }
    }

    void returnBook(int userId, int bookId) {
        if (borrowedBooks.count(bookId) && borrowedBooks[bookId] == userId) {
            borrowedBooks.erase(bookId);
        }
    }

private:
    unordered_map<int, string> books;
    unordered_map<int, string> users;
    unordered_map<int, int> borrowedBooks;
};

// Multiple smaller classes implementation
class Book {
public:
    Book(int bookId, const string &title) : bookId(bookId), title(title), isBorrowed(false) {}
    bool isBorrowed;
    int bookId;
    string title;
};

class User {
public:
    User(int userId, const string &name) : userId(userId), name(name) {}
    int userId;
    string name;
};

class Library {
public:
    void addBook(int bookId, const string &title) {
        books[bookId] = new Book(bookId, title);
    }

    void addUser(int userId, const string &name) {
        users[userId] = new User(userId, name);
    }

    void borrowBook(int userId, int bookId) {
        if (books.count(bookId) && users.count(userId)) {
            Book *book = books[bookId];
            if (!book->isBorrowed) {
                book->isBorrowed = true;
                borrowedBooks[bookId] = userId;
            }
        }
    }

    void returnBook(int userId, int bookId) {
        if (borrowedBooks.count(bookId) && borrowedBooks[bookId] == userId) {
            Book *book = books[bookId];
            book->isBorrowed = false;
            borrowedBooks.erase(bookId);
        }
    }

private:
    unordered_map<int, Book *> books;
    unordered_map<int, User *> users;
    unordered_map<int, int> borrowedBooks;
};

void measurePerformance(auto &library) {
    // Add a large number of books and users
    for (int bookId = 1; bookId <= 1000; ++bookId) {
        library.addBook(bookId, "Book " + to_string(bookId));
    }

    for (int userId = 1; userId <= 500; ++userId) {
        library.addUser(userId, "User " + to_string(userId));
    }

    // Perform borrow and return operations multiple times
    for (int i = 0; i < 10; ++i) {
        for (int userId = 1; userId <= 500; ++userId) {
            for (int bookId = 1; bookId <= 1000; ++bookId) {
                library.borrowBook(userId, bookId);
                library.returnBook(userId, bookId);
            }
        }
    }
}

int main() {
    // Measure performance of the single large class implementation
    LibrarySystem librarySystem;
    auto start = chrono::high_resolution_clock::now();
    measurePerformance(librarySystem);
    auto end = chrono::high_resolution_clock::now();
    cout << "Single large class implementation execution time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms" << endl;

    // Measure performance of the multiple smaller classes implementation
    Library library;
    start = chrono::high_resolution_clock::now();
    measurePerformance(library);
    end = chrono::high_resolution_clock::now();
    cout << "Multiple smaller classes implementation execution time: "
         << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms" << endl;

    return 0;
}
