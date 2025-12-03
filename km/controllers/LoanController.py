import json
import datetime

class LoanController:
    """"""
    
    def loan(self, isbn, document):
        list_books = []
        
        with open("data/books.json", "r")as file:
            list_books = json.load(file)
            
        
        found_book = None
        
        for book in list_books:
            if book['isbn'] == isbn:
                found_book = book
                
        list_users = []
        
        with open("data/users.json") as file:
            list_users = json.load(file)
        
        found_user = None
        
        for user in list_users:
            if user['document'] == document:
                found_user = user
        
        if found_book['stock'] > 0:
            found_book['stock'] -= 1

            now = datetime.datetime.now()
            hour = now.strftime("%Y-%m-%d %H:%M:%S") 
        
            format_data = {
                "isbn": found_book['isbn'],
                "document": found_user['document'],
                "date": hour
            }
            
            found_user['history'].append(format_data)

        else:
            if document not in found_book['reservations']:
                found_book['reservations'].append(document) 
            else:
                print("This user is already in reservations.")
                
        with open("data/books.json", "w") as file:
            json.dump(list_books, file, indent=4)
            
        with open("data/users.json", "w") as file:
            json.dump(list_users, file, indent=4)
            
        ordered_list = []
        
        with open("data/books_ordered.json", "r") as file:
            ordered_list = json.load(file)
        
        for b in ordered_list:
            if b['isbn'] == isbn:
                b['stock'] == found_book['stock']
                b['reservations'] = found_book['reservations']
                
        with open("data/books_ordered.json", "w") as file:
            json.dump(ordered_list, file, indent=4)
        
    def return_book(self, isbn):
        
        list_books = []
        
        with open("data/books.json", "r") as file:
            list_books = json.load(file)
        
        list_users = []
        
        with open("data/users.json", "r") as file:
            list_users = json.load(file)       
        
        found_book = None
        
        for book in list_books:
            if book['isbn'] == isbn:
                found_book = book
        
        if len(found_book['reservations']) > 0:
            document = found_book['reservations'].pop(0)

            found_user = None
        
            for user in list_users:
                if user['document'] == document:
                    found_user = user
                    break
            
            if found_user:
                
                date = datetime.datetime.now()
                hour = date.strftime("%Y-%m-%d %H:%M:%S") 
                
                loan_data = {
                    "isbn": found_book['isbn'],
                    "document": found_user['document'],
                    "date": hour
                }
                
                found_user['history'].append(loan_data)
        
        else:
            found_book['stock'] += 1
        
        with open("data/books.json", "w") as file:
            json.dump(list_books, file, indent=4)
     
        with open("data/users.json", "w") as file:
            json.dump(list_users, file, indent=4)                         