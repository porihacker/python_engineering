class Book:
    total_number_books = 0  

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # Initialize as not checked out
        Book.total_number_books += 1  # Increment the total number of books

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."

    @classmethod
    def get_total_books(cls):
        return f"Total number of books are {cls.total_number_books}"

# Example usage
book1 = Book('Alchemist', 'Paulo Coelho', 'isbn726216')
book2 = Book('Get Rich die tryin', '50 Cent', 'isbn7663')

print(book1.checkout())
print(book1.return_book())
print(Book.get_total_books())