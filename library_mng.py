class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def __str__(self):
        return f"{self.title}, {self.author} and {self.year}"


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre


class NonFictionBook(Book):
    def __init__(self, title, author, year, subject):
        super().__init__(title, author, year)
        self.subject = subject


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("This book is not an instance of Book class")
        else:
            is_in_dict = self.books.get(book.title, False)
            if not is_in_dict:
                self.books[book.title] = book
            else:
                raise ValueError(f"This book '{book.title}' is already added to this library")

    def remove_book(self, book_title):
        if book_title in self.books:
            del self.books[book_title]
        else:
            raise KeyError(f"This book with title of '{book_title}' not found in the library")

    def search_books_by_author(self, book_author):
        book_search = []
        for book_t, book_obj in self.books.items():
            if book_obj.author == book_author:
                book_search.append(book_t)
        if not book_search:
            raise ValueError(f"This author '{book_author}' has no book in this library")
        return book_search

    def checkout_book(self, book_title):
        if self.books[book_title].available:
            self.books[book_title].available = False
        else:
            raise Exception(f"The book '{book_title}' that you want to check out is not available")

    def return_book(self, book_title):
        if not self.books[book_title].available:
            self.books[book_title].available = True
        else:
            raise Exception(f"The book '{book_title}' that you want to check out was checked out")


def main():

    library = Library()

    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    book2 = NonFictionBook("Sapiens", "Yuval Noah Harari", 2011, "History")
    book3 = FictionBook("Harry Potter", "J.K. Rowling", 1997, "Fantasy")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Try adding a duplicate book
    try:
        library.add_book(book1)
    except ValueError as e:
        print(e)

    # Search books by author
    print("Books by J.K. Rowling:", library.search_books_by_author("J.K. Rowling"))

    # Checkout a book
    library.checkout_book("Harry Potter")

    # Try to check out an already checked-out book
    try:
        library.checkout_book("Harry Potter")
    except Exception as e:
        print(e)

    # Return the book
    library.return_book("Harry Potter")

    # Remove a book
    library.remove_book("Sapiens")

    # Try removing a non-existent book
    try:
        library.remove_book("Non-existent Book")
    except KeyError as e:
        print(e)


if __name__ == "__main__":
    main()