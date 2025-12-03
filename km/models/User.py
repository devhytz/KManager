class User:
    """
    This class represents an common virtual user with some attributes and actions.
    
    Initializer: 
        variable = User(document, name).

    Atr: 
        document: str,  len > 0 and < 11.
        name: str, len > 0 and < 51.
        
    Meths:
        object.getAttribute() -> returns attribute.
        object.setAttribute(object, value) -> update attribute.
        object.showUser() -> shows all attributes.
        
    """
    # Atributtes for default 
    
    document = "Unknow"
    name = "Unknow"        
    
    def __init__(self, document, name):    # Constructor to make instances
        self.document = document
        self.name = name                 
        self.history = []   # List to save the history of loans 
    
    # Methods to get and set attributes
    
    def getDocument(self):     
        return self.document
    
    def setDocument(self, document):
        if len(document) > 0 and len(document) < 11 and str.isdigit(document): 
            self.document = document            
        else:
            if str.isdigit(document) == False:      
                raise TypeError("Document must be numbers.") # Document can´t be digits in Colombia
            if len(document) < 1 or len(document) > 10:
                raise ValueError("Document must be between 1 and 10 digits") # Length average in Colombia
        
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        if len(name) > 0 and len(name) < 51 and str.isdigit(name):    
            self.name = name           
        else:
            if str.isalpha(name) == False:      
                raise TypeError("Name must be letters without space") # Name only can be digits
            if len(name) < 1 or len(name) > 51:
                raise ValueError("Name must be between 1 and 51 digits")
    
   
    def showUser(self):
        print(f"Document: {self.document}")
        print(f"Name: {self.name}")
        print(f"")
        
    def __str__(self):
        return f"{self.name} {self.document}"

      

