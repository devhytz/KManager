class Book:
    """
    This class represents an book that belongs to a library.
    
    Initializer:
        variable = Book(isbn, title, autor, value, weight).
    
    Atr: 
        isbn: str,  len = 13 .
        title: str, len > 0 and < 71.
        autor: str, len > 0 and < 51.
        value: int, value > 0 and <= 10000000 (COP Terms)
        weight: float, value > 0 and <= 8 (Kg Terms)
    
    Meths: 
    
    """
    
    isbn = "Unknow"
    title = "Unknow"
    autor = "Unkown"
    value = "Unkown"
    weight = "Unkown"
    
    def __init__(self, isbn, title, autor, value, weight):
        self.isbn = isbn
        self.title = title
        self.autor = autor
        self.value = value
        self.weight = weight
        
    # Methods to get and set of isbn attribute
    
    def getIsbn(self):
        return self.isbn
    
    def setIsbn(self, isbn):
        if len(isbn) == 10 and str.isdigit(isbn):
            self.isbn = isbn
        else:
            raise ValueError("ISBN Code must be 10 numbers")
    
    # Methods to get and set of title attribute
    
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        if len(title) > 0 and len(title)< 71:
            self.title = title
        else:
            raise ValueError("Title must be between 1 and 70 characters")

    # Methods to get and set of autor attribute
    
    def getAutor(self):
        return self.title
    
    def setAutor(self, autor):
        if len(autor) > 0 and len(autor) < 51:
            self.autor = autor
        else:
            raise ValueError("Tutor must be between 1 and 50 characters")
    
    # Methods to get and set of value attribute
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        if value > 0 and value < 10000000:
            self.value = value
        else:
            raise ValueError("Value must be between $1 (COP) and $10000000 (COP)")
    
    # Methods to get and set of weight attribute
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        if weight > 0 and weight < 8.00:
            self.weight = weight
        else:
            raise ValueError("Weight must be between 0.001 (LB) and 8(KG)")
        
    
    