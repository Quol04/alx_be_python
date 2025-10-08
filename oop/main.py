from book_class import Book

def main():
    # creating an instance of the Book 
    my_book = Book("1984", "George Orwell",1949)

    # demonstrating the __str__ method
    print(my_book) #expected to use the __str__ method

    # demonstrating the __repr__ method
    print(repr(my_book)) #expected to use the __repr__ method

    # deleting a book instance to trigger the __del__ method
    del my_book

if __name__ == "__main__":
    main()
