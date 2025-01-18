package main

import (
	"fmt"
	"time"
)

// Single large struct implementation
type LibrarySystem struct {
	books         map[int]string
	users         map[int]string
	borrowedBooks map[int]int
}

func NewLibrarySystem() *LibrarySystem {
	return &LibrarySystem{
		books:         make(map[int]string),
		users:         make(map[int]string),
		borrowedBooks: make(map[int]int),
	}
}

func (ls *LibrarySystem) AddBook(bookID int, title string) {
	ls.books[bookID] = title
}

func (ls *LibrarySystem) AddUser(userID int, name string) {
	ls.users[userID] = name
}

func (ls *LibrarySystem) BorrowBook(userID, bookID int) {
	if _, bookExists := ls.books[bookID]; bookExists {
		if _, userExists := ls.users[userID]; userExists {
			if _, alreadyBorrowed := ls.borrowedBooks[bookID]; !alreadyBorrowed {
				ls.borrowedBooks[bookID] = userID
			}
		}
	}
}

func (ls *LibrarySystem) ReturnBook(userID, bookID int) {
	if borrower, borrowed := ls.borrowedBooks[bookID]; borrowed && borrower == userID {
		delete(ls.borrowedBooks, bookID)
	}
}

// Multiple smaller structs implementation
type Book struct {
	ID        int
	Title     string
	IsBorrowed bool
}

type User struct {
	ID   int
	Name string
}

type Library struct {
	books         map[int]*Book
	users         map[int]*User
	borrowedBooks map[int]int
}

func NewLibrary() *Library {
	return &Library{
		books:         make(map[int]*Book),
		users:         make(map[int]*User),
		borrowedBooks: make(map[int]int),
	}
}

func (l *Library) AddBook(bookID int, title string) {
	l.books[bookID] = &Book{ID: bookID, Title: title, IsBorrowed: false}
}

func (l *Library) AddUser(userID int, name string) {
	l.users[userID] = &User{ID: userID, Name: name}
}

func (l *Library) BorrowBook(userID, bookID int) {
	if book, bookExists := l.books[bookID]; bookExists {
		if !book.IsBorrowed {
			if _, userExists := l.users[userID]; userExists {
				book.IsBorrowed = true
				l.borrowedBooks[bookID] = userID
			}
		}
	}
}

func (l *Library) ReturnBook(userID, bookID int) {
	if borrower, borrowed := l.borrowedBooks[bookID]; borrowed && borrower == userID {
		if book, exists := l.books[bookID]; exists {
			book.IsBorrowed = false
		}
		delete(l.borrowedBooks, bookID)
	}
}

func measurePerformance(library interface{}) {
	switch lib := library.(type) {
	case *LibrarySystem:
		for bookID := 1; bookID <= 1000; bookID++ {
			lib.AddBook(bookID, fmt.Sprintf("Book %d", bookID))
		}
		for userID := 1; userID <= 500; userID++ {
			lib.AddUser(userID, fmt.Sprintf("User %d", userID))
		}
		for i := 0; i < 10; i++ {
			for userID := 1; userID <= 500; userID++ {
				for bookID := 1; bookID <= 1000; bookID++ {
					lib.BorrowBook(userID, bookID)
					lib.ReturnBook(userID, bookID)
				}
			}
		}
	case *Library:
		for bookID := 1; bookID <= 1000; bookID++ {
			lib.AddBook(bookID, fmt.Sprintf("Book %d", bookID))
		}
		for userID := 1; userID <= 500; userID++ {
			lib.AddUser(userID, fmt.Sprintf("User %d", userID))
		}
		for i := 0; i < 10; i++ {
			for userID := 1; userID <= 500; userID++ {
				for bookID := 1; bookID <= 1000; bookID++ {
					lib.BorrowBook(userID, bookID)
					lib.ReturnBook(userID, bookID)
				}
			}
		}
	}
}

func main() {
	// Measure performance of the single large struct implementation
	librarySystem := NewLibrarySystem()
	singleClassTime := time.Now()
	measurePerformance(librarySystem)
	fmt.Printf("Single large struct implementation execution time: %v\n", time.Since(singleClassTime))

	// Measure performance of the multiple smaller structs implementation
	library := NewLibrary()
	multipleClassTime := time.Now()
	measurePerformance(library)
	fmt.Printf("Multiple smaller structs implementation execution time: %v\n", time.Since(multipleClassTime))
}
