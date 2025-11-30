from pathlib import Path
import json
from km.models.Book import Book
class BookController:
    """ DOC NO YET
    """
    
    # ------------------------ Auxiliar Methods -------------------------
    def verify_file(self):
        route = Path("data/books.json")
        
        if route.is_file():
            return True
        else:
            # Lista vacia
            print("File does not exist... creating.")
            
            create = []
            
            with open("data/books.json", "w") as file:
                json.dump(create, file, indent=4)
        
    
    # ----------------------------------- CRUD --------------------------
    #"data/books.json" - Ruta archivo books.json
    
    def searching(self, isbn):
        # Lista en la cual se guardará el contenido del archivo
        list_books = []
            
        with open("data/books.json", "r") as file:
            list_books = json.load(file)
            
        # Recorrer la lista e identificar el ISBN de cada libro
        for book in list_books:
            if book['isbn'] == isbn:
                return True
              
                
    def add_book(self, new_book):
        # Verificar si existe el archivo
        if self.verify_file():
            if not self.searching(new_book):
                list_books = []
                
                # Traer informacion desde el archivo hasta una variable
                with open("data/books.json", "r") as file:
                    list_books = json.load(file)
                    
                # Pasarlo a formato json
                format = {
                    "isbn" : new_book.isbn,
                    "title" : new_book.title,
                    "author" : new_book.author,
                    "value" : new_book.value,
                    "weight" : new_book.weight
                    
                }
                
                # Meter el nuevo usuario en la lista
                list_books.append(format)
                
                # Pasar la nueva lista con el usuario añadido al archivo
                with open("data/books.json", "w") as file:
                    json.dump(list_books, file, indent=4)  
                
                print(f"{format['title']} added")     
            else:
                return print(f"Error, {new_book.title} already exists.")
        
             
    def search_book(self, isbn):
        
        if self.verify_file():
            if self.searching(isbn):
                # Traemos la informacion a la lista vacia
                list_books = []
                
                with open("data/books.json", "r") as file:
                    list_books = json.load(file)
                    
                    for b in list_books:
                        if b['isbn'] == isbn:
                            print("This book already exists: ")
                            print("")
                            print(f"ISBN: {b['isbn']}")
                            print(f"Title: {b['title']}")
                            print(f"author: {b['author']}")
                            print(f"Value: {b['value']}")
                            print(f"Weight: {b['weight']}")
                        return True
            else:
                return print(f"The book with ISBN code: {isbn} does not exists.")
                        
        
   
    def list_books(self):
        if self.verify_file():
            list_books = []
            
            with open("data/books.json", "r") as file:
                list_books = json.load(file)
                
            for book in list_books:
                
                # Imprime cada atributo para que se vea ordenado y los espacios por legibilidad
                print("")
                print(f"ISBN: {book['isbn']}")
                print(f"Title: {book['title']}")
                print(f"author: {book['author']}")
                print(f"Value: {book['value']}")
                print(f"Weight: {book['weight']}")
                print("")
        
        
    
    
    def update_book(self, book):
        # Lista en la cual traemos la informacion
        list_books = []
        
        # Verificamos si el usuario realmente existe en el archivo
        if self.searching(book):
            with open("data/books.json", "r") as file:
                list_books = json.load(file)
            
            # Recorremos hasta encontrar el usuario
            for b in list_books:
                if b['isbn'] == book.isbn:
                    
                    # Preguntamos que dato/s se desean actualizar
                    print("1) To change ISBN code")
                    print("2) To change title")
                    print("3) To change author")
                    print("4) To change value")
                    print("5) To change weight")
                    print("6) To change all")
                    option = int(input("Select an option: "))
                    
                    match option:
                        case 1:
                            new_isbn = input("Introduce the new ISBN code: ")
                            b['isbn'] = new_isbn
                            print(f"{b['isbn']} updated")
                        case 2:
                            new_title = input("Introduce the new title: ")
                            b['title'] = new_title
                            print(f"{b['title']} updated")
                        case 3:
                            new_author = input("Introduce the new author name: ")
                            b['author'] = new_author
                            print(f"{b['author']} updated")
                        case 4:
                            new_value = input("Introduce the new value: ")
                            b['value'] = new_value
                            print(f"{b['value']} updated")
                        case 5:
                            new_weight = input("Introduce the new weight value: ")
                            b['weight'] = new_weight
                            print(f"{b['weight']} updated")
                        case 6:
                            new_isbn = input("Introduce the new ISBN code: ")
                            b['isbn'] = new_isbn
                            print(f"{b['isbn']} updated")
                            
                            new_title = input("Introduce the new title: ")
                            b['title'] = new_title
                            print(f"{b['title']} updated")
                            
                            new_author = input("Introduce the new author name: ")
                            b['author'] = new_author
                            print(f"{b['author']} updated")
                            
                            new_value = input("Introduce the new value: ")
                            b['value'] = new_value
                            print(f"{b['value']} updated")
                            
                            new_weight = input("Introduce the new weight value: ")
                            b['weight'] = new_weight
                            print(f"{b['weight']} updated")
                            
                            print("")
                            print("Success")
                            print("")
                            
                        case _:
                            print("Invalid option")
                
                    # Enviamos la lista actualizada al archivo
                    with open("data/books.json", "w") as file:
                        json.dump(list_books, file, indent=4)
                    
                        
                    break
                
        else:
            return print(f"{book.name} does not exist") 
    
    def delete_book(self, isbn):
        if self.verify_file():
        
                list_books = []
                
                with open("data/books.json", "r") as file:
                    list_books = json.load(file)
                
                new_list = []
                
                for book in list_books:
                    if book['isbn'] != isbn:
                        new_list.append(book)
                
                with open("data/books.json", "w") as file:
                    json.dump(new_list, file, indent=4)
                    
                return print(f"The book with ISBN code: {isbn} was deleted")
            
                
            
            
            