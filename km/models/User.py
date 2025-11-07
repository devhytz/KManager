class User:
    """
    This class represents an common virtual user with some attributes and actions.
    
    Initializer: 
        variable = User(document, name, mail, password).

    Atr: 
        document: str,  len > 0 and < 11.
        name: str, len > 0 and < 51.
        mail: str, must contains "@" format.
        password: str, len > 8 and < 21
        
    Meths:
        object.getAttribute() -> returns attribute.
        object.setAttribute(object, value) -> update attribute.
        object.showUser() -> shows all attributes.
        
    """
    
    document = "Unknow"
    name = "Unknow"      # This values are for default
    mail = "Unknow"    
    password = "Unknow"
    
    def __init__(self, document, name, mail, password):     # Constructor method to create an instance
        self.document = document
        self.name = name                 # This variables assigns the value to the instance
        self.mail = mail
        self.password = password
        
    # Methods to access and set of document attribute
    
    def getDocument(self):      # Access to the name of the instance and return it
        return self.document
    
    def setDocument(self, document):
        if len(document) > 0 and len(document) < 11 and str.isdigit(document):    # Conditional to assign
            self.document = document            # Updates the value
        else:
            if str.isdigit(document) == False:      # Verify error type and throw the message for it
                raise TypeError("Document must be numbers.")
            if len(document) < 1 or len(document) > 10:
                raise ValueError("Document must be between 1 and 10 digits")
        
    # Methods to access and set of name attribute
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        if len(name) > 0 and len(name) < 51 and str.isdigit(name):    # Conditional to assign
            self.document = name            # Updates the value
        else:
            if str.isalpha(name) == False:      # Verify error type and throw the message for it
                raise TypeError("Name must be letters without space")
            if len(name) < 1 or len(name) > 51:
                raise ValueError("Name must be between 1 and 51 digits")
    
    # Methods to access and set of mail attribute
    
    def getMail(self):
        return self.mail
    
    def setMail(self, mail):
        if "@" in mail:
            self.mail = mail
        else:
            raise ValueError("Mail must contain @ in the format")
        
    # Methods to access, comprobation of a valid password and set it
    
    def getPassword(self):
        return self.password
    
    def validPass(self, password):
        hasLetters = any(char.isalpha() for char in password)
        hasNumbers = any(char.isdigit() for char in password)
        return hasLetters and hasNumbers

    def setPassword(self, password):
        if self.validPass(password):
            self.password = password
        else:
            raise ValueError("Password must contain letters and numbers")

        
