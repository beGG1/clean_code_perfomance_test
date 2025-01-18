import kotlin.system.measureTimeMillis

// Single large class implementation
class LibrarySystem {
    private val books = mutableMapOf<Int, String>()
    private val users = mutableMapOf<Int, String>()
    private val borrowedBooks = mutableMapOf<Int, Int>()

    fun addBook(bookId: Int, title: String) {
        books[bookId] = title
    }

    fun addUser(userId: Int, name: String) {
        users[userId] = name
    }

    fun borrowBook(userId: Int, bookId: Int) {
        if (books.containsKey(bookId) && users.containsKey(userId)) {
            if (!borrowedBooks.containsKey(bookId)) {
                borrowedBooks[bookId] = userId
            }
        }
    }

    fun returnBook(userId: Int, bookId: Int) {
        if (borrowedBooks[bookId] == userId) {
            borrowedBooks.remove(bookId)
        }
    }
}

// Multiple smaller classes implementation
class Book(val bookId: Int, val title: String) {
    var isBorrowed: Boolean = false
}

class User(val userId: Int, val name: String)

class Library {
    private val books = mutableMapOf<Int, Book>()
    private val users = mutableMapOf<Int, User>()
    private val borrowedBooks = mutableMapOf<Int, Int>()

    fun addBook(bookId: Int, title: String) {
        books[bookId] = Book(bookId, title)
    }

    fun addUser(userId: Int, name: String) {
        users[userId] = User(userId, name)
    }

    fun borrowBook(userId: Int, bookId: Int) {
        val book = books[bookId]
        if (book != null && !book.isBorrowed && users.containsKey(userId)) {
            book.isBorrowed = true
            borrowedBooks[bookId] = userId
        }
    }

    fun returnBook(userId: Int, bookId: Int) {
        if (borrowedBooks[bookId] == userId) {
            val book = books[bookId]
            if (book != null) {
                book.isBorrowed = false
                borrowedBooks.remove(bookId)
            }
        }
    }
}

fun measurePerformance(library: Any) {
    when (library) {
        is LibrarySystem -> {
            for (bookId in 1..1000) {
                library.addBook(bookId, "Book $bookId")
            }
            for (userId in 1..500) {
                library.addUser(userId, "User $userId")
            }
            repeat(10) {
                for (userId in 1..500) {
                    for (bookId in 1..1000) {
                        library.borrowBook(userId, bookId)
                        library.returnBook(userId, bookId)
                    }
                }
            }
        }
        is Library -> {
            for (bookId in 1..1000) {
                library.addBook(bookId, "Book $bookId")
            }
            for (userId in 1..500) {
                library.addUser(userId, "User $userId")
            }
            repeat(10) {
                for (userId in 1..500) {
                    for (bookId in 1..1000) {
                        library.borrowBook(userId, bookId)
                        library.returnBook(userId, bookId)
                    }
                }
            }
        }
    }
}

fun main() {
    // Measure performance of the single large class implementation
    val librarySystem = LibrarySystem()
    val singleClassTime = measureTimeMillis {
        measurePerformance(librarySystem)
    }
    println("Single large class implementation execution time: $singleClassTime ms")

    // Measure performance of the multiple smaller classes implementation
    val library = Library()
    val multipleClassTime = measureTimeMillis {
        measurePerformance(library)
    }
    println("Multiple smaller classes implementation execution time: $multipleClassTime ms")
}
