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


class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado.")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuarion {user.name} ha sido registrado.")
    
    def show_available_books(self):
        print(f"Libros disponibles: ")
        for book in self.books:
            if book.availabel:
                print(f"\t - El libro {book.title} por {book.author}")
    
try: 
    # Creando books
    book1 = Book("Python a fondo", "Oscar Ramirez")
    book2 = Book("gRPC Go for Profesionals", "Clement Jean")
    book3 = Book("Microservices with Go", "Alexander Shuiskov")
    book4 = Book("Patrones de Diseño", "Alecxander Shvets")
    book5 = Book("Pro Go", "Adam Freeman")
    #Creando el usuario
    user1 = User("Fabian Beltran", 1 )
    #Crear la biblioteca
    library1 = Library()
    #Agregando libros
    library1.add_book(book1)
    library1.add_book(book2)
    library1.add_book(book3)
    library1.add_book(book4)
    library1.add_book(book5)
    library1.register_user(user1)

    #Mostrar libro
    library1.show_available_books()

    #Prestar libro.
    user1.borrow_book(book2)
    user1.borrow_book(book3)
    user1.borrow_book(book4)
    #Retornar libro
    user1.return_book(book2)

    library1.show_available_books()
    

except Exception as e:
    print(f"Woops!. Hubo un error: ", e)
    