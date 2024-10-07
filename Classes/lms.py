class Book:
    total_number_books = 0  

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False 
        Book.total_number_books += 1  

    def __str__(self) -> str:
        return f"{self.author}, {self.title}, {self.isbn}"
        

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




class Library:
    def __init__(self):
        self.books = []  
    


    def addBook(self, book):
        for i in self.books:

            if i.isbn==book.isbn:
                print("Book is already in  the library")
                return
            
        self.books.append(book)
        print("Book is added in  the library")

        

            

    
    def showBooks(self):
        if not self.books:
            print("No books in the Library please consider adding them")
        for i , book in enumerate(self.books, 1):
            print(f"{i}) {book} ")



newbook=Book('Steve Jobs', "Walter Isaacson", "1234ibn")
newbook1=Book('Steve Jobs', "Walter Isaacson", "1234ibn")
newbook2=Book('Power', "Courtney Kemp", "isbn34316q")


rosvilleLib= Library()
rosvilleLib.addBook(newbook)
rosvilleLib.addBook(newbook1)
rosvilleLib.addBook(newbook2)
rosvilleLib.showBooks()


