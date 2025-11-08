import datetime


class Manager:
    
    start_hour = 0
    finish_hour = 0
    
    def __init__(self, start_hour, finish_hour, user, book):
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.user = user
        self.book = book
    
    def getStart_hour(self):
        return self.start_hour
    
    def setStart_hour(self, start_hour):
        if not start_hour > datetime.datetime.now():
            self.start_hour = start_hour
        else:
            raise ValueError("The time cannot be a value higher than the current time.")
        
    def getFinish_hour(self):
        return self.finish_hour
    
    def setFinish_hour(self, finish_hour):
        if not finish_hour > datetime.datetime.now():
            self.start_hour = finish_hour
        else:
            raise ValueError("The time cannot be a value higher than the current time.")
    
    def getUser(self):
        return self.user
    
    def setUser(self, user):
        self.user = user
    
    def getBook(self):
        return self.book
    
    def setBook(self, book):
        self.book = book
        
    def showManager(self):
        print(f"Starting hour: {self.start_hour}")
        print(f"Finishing hour: {self.finish_hour}")
        print("")
        print(f"User: {self.user.showUser()}")
        print("")
        print(f"Book: {self.book.showBook()}")
        print("")