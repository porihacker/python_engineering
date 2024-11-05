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
    


    def addBook(self):
       title=input("Enter book name: ")
       author=input("Enter book author: ")
       isbn=input("Enter book isbn: ")

       for book in self.books:
           if isbn==book.isbn:
               print(f"The book with this {isbn} already exist")
               return
    

       new_book=Book(title,author,isbn)

       self.books.append(new_book)
       print(f"{title} has been added to the library")
            
               



        

            

    
    def showBooks(self):
        if not self.books:
            print("No books in the Library please consider adding them")
        for i , book in enumerate(self.books, 1):
            print(f"{i}) {book} ")

    def check_out_book(self,isbn):
    
        book_to_checkout=None;

        for book in self.books:
            if book.isbn == isbn:
                book_to_checkout=book
                break
        
        if book_to_checkout:
            print(book_to_checkout.checkout())
            self.books.remove(book_to_checkout)
        else:
            print("No book with {isbn}")

    def  return_book(self,isbn):
        book_to_return=None;

        for book in self.books:
            if book.isbn == isbn:
               
               book_to_return=book
        

        









creating_a_book=True

while creating_a_book:
   




    rosvilleLib= Library()
    rosvilleLib.addBook()
    rosvilleLib.showBooks()
 



