class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def __str__(self):
        status = "Checked Out" if self.__is_checked_out else "Available"
        return f"'{self.title}' by {self.author} - {status}"
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book._Book__is_checked_out]
        for book in available_books:
            print(book)
        if not available_books:
            print("No books are currently available.")

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and not book._Book__is_checked_out:
                book._Book__is_checked_out = True
                print(f"You have checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book._Book__is_checked_out:
                book._Book__is_checked_out = False
                print(f"You have returned '{title}'.")
                return
        print(f"'{title}' was not checked out from this library.")