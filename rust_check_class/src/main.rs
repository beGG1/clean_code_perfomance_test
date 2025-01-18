use std::collections::HashMap;
use std::time::Instant;

// Single large struct implementation
struct LibrarySystem {
    books: HashMap<i32, String>,
    users: HashMap<i32, String>,
    borrowed_books: HashMap<i32, i32>,
}

impl LibrarySystem {
    fn new() -> Self {
        Self {
            books: HashMap::new(),
            users: HashMap::new(),
            borrowed_books: HashMap::new(),
        }
    }

    fn add_book(&mut self, book_id: i32, title: String) {
        self.books.insert(book_id, title);
    }

    fn add_user(&mut self, user_id: i32, name: String) {
        self.users.insert(user_id, name);
    }

    fn borrow_book(&mut self, user_id: i32, book_id: i32) {
        if self.books.contains_key(&book_id) && self.users.contains_key(&user_id) {
            if !self.borrowed_books.contains_key(&book_id) {
                self.borrowed_books.insert(book_id, user_id);
            }
        }
    }

    fn return_book(&mut self, user_id: i32, book_id: i32) {
        if self.borrowed_books.get(&book_id) == Some(&user_id) {
            self.borrowed_books.remove(&book_id);
        }
    }
}

// Multiple smaller structs implementation
struct Book {
    book_id: i32,
    title: String,
    is_borrowed: bool,
}

impl Book {
    fn new(book_id: i32, title: String) -> Self {
        Self {
            book_id,
            title,
            is_borrowed: false,
        }
    }
}

struct User {
    user_id: i32,
    name: String,
}

impl User {
    fn new(user_id: i32, name: String) -> Self {
        Self { user_id, name }
    }
}

struct Library {
    books: HashMap<i32, Book>,
    users: HashMap<i32, User>,
    borrowed_books: HashMap<i32, i32>,
}

impl Library {
    fn new() -> Self {
        Self {
            books: HashMap::new(),
            users: HashMap::new(),
            borrowed_books: HashMap::new(),
        }
    }

    fn add_book(&mut self, book_id: i32, title: String) {
        self.books.insert(book_id, Book::new(book_id, title));
    }

    fn add_user(&mut self, user_id: i32, name: String) {
        self.users.insert(user_id, User::new(user_id, name));
    }

    fn borrow_book(&mut self, user_id: i32, book_id: i32) {
        if let Some(book) = self.books.get_mut(&book_id) {
            if !book.is_borrowed {
                book.is_borrowed = true;
                self.borrowed_books.insert(book_id, user_id);
            }
        }
    }

    fn return_book(&mut self, user_id: i32, book_id: i32) {
        if let Some(borrower) = self.borrowed_books.get(&book_id) {
            if *borrower == user_id {
                if let Some(book) = self.books.get_mut(&book_id) {
                    book.is_borrowed = false;
                }
                self.borrowed_books.remove(&book_id);
            }
        }
    }
}

fn measure_performance<T: LibraryOps>(library: &mut T) {
    for book_id in 1..=1000 {
        library.add_book(book_id, format!("Book {}", book_id));
    }

    for user_id in 1..=500 {
        library.add_user(user_id, format!("User {}", user_id));
    }

    for _ in 0..10 {
        for user_id in 1..=500 {
            for book_id in 1..=1000 {
                library.borrow_book(user_id, book_id);
                library.return_book(user_id, book_id);
            }
        }
    }
}

trait LibraryOps {
    fn add_book(&mut self, book_id: i32, title: String);
    fn add_user(&mut self, user_id: i32, name: String);
    fn borrow_book(&mut self, user_id: i32, book_id: i32);
    fn return_book(&mut self, user_id: i32, book_id: i32);
}

impl LibraryOps for LibrarySystem {
    fn add_book(&mut self, book_id: i32, title: String) {
        self.add_book(book_id, title);
    }

    fn add_user(&mut self, user_id: i32, name: String) {
        self.add_user(user_id, name);
    }

    fn borrow_book(&mut self, user_id: i32, book_id: i32) {
        self.borrow_book(user_id, book_id);
    }

    fn return_book(&mut self, user_id: i32, book_id: i32) {
        self.return_book(user_id, book_id);
    }
}

impl LibraryOps for Library {
    fn add_book(&mut self, book_id: i32, title: String) {
        self.add_book(book_id, title);
    }

    fn add_user(&mut self, user_id: i32, name: String) {
        self.add_user(user_id, name);
    }

    fn borrow_book(&mut self, user_id: i32, book_id: i32) {
        self.borrow_book(user_id, book_id);
    }

    fn return_book(&mut self, user_id: i32, book_id: i32) {
        self.return_book(user_id, book_id);
    }
}

fn main() {
    let mut library_system = LibrarySystem::new();
    let start = Instant::now();
    measure_performance(&mut library_system);
    println!("Single large struct implementation execution time: {:?}", start.elapsed());

    let mut library = Library::new();
    let start = Instant::now();
    measure_performance(&mut library);
    println!("Multiple smaller structs implementation execution time: {:?}", start.elapsed());
}
