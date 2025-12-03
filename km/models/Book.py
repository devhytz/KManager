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
        stock: int
        
    Meths:
        object.getAttribute() -> returns attribute.
        object.setAttribute(object, value) -> update attribute.
        object.showBook() -> shows all attributes.
        
    """
    # Attributes for default
    
    isbn = "Unknow"
    title = "Unknow"      
    author = "Unknow"    
    value = 0
    weight = 0.0
    stock = 0
    
    # Getters and setters method for the attributes
    
    def getIsbn(self):      
        return self.isbn
    
    def setIsbn(self, isbn):
        if str.isdigit(isbn):
            if len(isbn) == 10: 
                self.isbn = isbn
            else:
                raise ValueError("ISBN must be exactly 10 digits") # The ISBN of the books are 10 digits
        else:
            raise TypeError("ISBN must be numbers") # An ISBN code must be of numbers
        
        
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        if len(title) > 0 and len(title) < 100:   # Title can´t be blank
            self.title = title          
        else:
            raise ValueError("Title must be between 1 and 100 characters")
        
        
    def getAuthor(self):
        return self.author
    
    def setAuthor(self, author):
        if len(author) > 0 and len(author) < 51: # Author´s name its neccesary to assign on the object
            self.author = author
        else:
            raise ValueError("Author name must be between 1 and 50 characters")
        
        
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        value = int(value)
        if value > 0:
                self.value = value
        else:
            raise ValueError("Value must be a positive number") # Number > 0 
      

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        try:
            weight = float(weight)
            if weight > 0:
                self.weight = weight
            else:
                raise ValueError("Weight must be greater than 0")
        except ValueError:
            raise TypeError("Weight must be a number (float)") # Float to representate Kg format
    
    def __init__(self, isbn, title, author, value, weight, stock):  # Constructor for the instances
        self.setIsbn(isbn)  # To validate the attributes of the new object
        self.setTitle(title)
        self.setAuthor(author)
        self.setValue(value)
        self.setWeight(weight)
        self.stock = stock
        self.reservations = [] # List where it contains registers of reservations
        
    
    def showBook(self):
        print(f"ISBN: {self.isbn}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Value: ${self.value}")
        print(f"Weight: {self.weight} Kg")
        print(f"")
        
        
    def __str__(self):
        return f"{self.title} - {self.author}"