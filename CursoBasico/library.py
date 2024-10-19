class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self.availabel = True
    
    def borrow(self):
        if self.availabel:
            self.availabel = False
            print(f"El libro {self.title} se te esta prestando")
        else:
            print(f"El libro {self.title} no esta disponible en el momento.")

    def return_book(self):
        self.availabel = True
        print(f"Gracias por devolver el libro: {self.title}.")

class User:
    def __init__(self, name, user_id) -> None:
        self.name = name
        self.user_id = user_id
        self.borrowed_books = list()

    def borrow_book(self, book):
        if book.availabel:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} No esta disponible")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No esta en la lista de prestados")