class Book:
    """
    This class represents a book that belongs to the library inventory.
    
    Initializer: 
        variable = Book(isbn, title, author, value, weight).

    Atr: 
        isbn: str, len > 0 and < 14 (should be digits).
        title: str, len > 0 and < 100.
        author: str, len > 0 and < 51.
        value: int, must be > 0 (COP currency).
        weight: float, must be > 0 (Kg).
        
    Meths:
        object.getAttribute() -> returns attribute.
        object.setAttribute(object, value) -> update attribute.
        object.showBook() -> shows all attributes.
        
    """
    
    isbn = "Unknow"
    title = "Unknow" 
    author = "Unknow" 
    value = 0
    weight = 0.0
    
    # Methods to access and set of isbn attribute
    
    def getIsbn(self): 
        return self.isbn
    
    def setIsbn(self, isbn):
        if len(isbn) > 0 and len(isbn) < 14 and str.isdigit(isbn): 
            self.isbn = isbn 
        else:
            if str.isdigit(isbn) == False:
                raise TypeError("ISBN must be numbers")
            if len(isbn) < 1 or len(isbn) > 13:
                raise ValueError("ISBN must be between 1 and 13 digits")
        
    # Methods to access and set of title attribute
    
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        if len(title) > 0 and len(title) < 100:
            self.title = title
        else:
            raise ValueError("Title must be between 1 and 100 characters")
    
    # Methods to access and set of author attribute
    
    def getAuthor(self):
        return self.author
    
    def setAuthor(self, author):
        if len(author) > 0 and len(author) < 51:
            self.author = author
        else:
            raise ValueError("Author name must be between 1 and 50 characters")
        
    # Methods to access and set of value attribute 
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        try:
            value = int(value)
            if value > 0:
                self.value = value
            else:
                raise ValueError("Value must be a positive number")
        except ValueError:
             raise TypeError("Value must be a number")

    # Methods to access and set of weight attribute

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        # We verify if is float for kilograms
        try:
            weight = float(weight)
            if weight > 0:
                self.weight = weight
            else:
                raise ValueError("Weight must be greater than 0")
        except ValueError:
            raise TypeError("Weight must be a number (float)")
    
    
    def __init__(self, isbn, title, author, value, weight):  
        
        # ⚠️ MODIFICACIÓN APLICADA AQUÍ ⚠️
        # Se eliminaron las asignaciones directas y solo se usan los setters.
        
        # We call the setters to validate data inside the constructor
        self.setIsbn(isbn)
        self.setTitle(title)
        self.setAuthor(author)
        self.setValue(value)
        self.setWeight(weight)
        
    

    def showBook(self):
        print(f"ISBN: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Value: ${self.value}")
        print(f"Weight: {self.weight} Kg")
        print(f"")
        
    def __str__(self):
        return f"{self.title} - {self.author}"