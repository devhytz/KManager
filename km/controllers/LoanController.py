import json
import datetime

class LoanController:
    """
    LoanController

    This class manages all loan and return operations for the library system.
    It handles:
        - Registering new loans.
        - Managing user loan history.
        - Handling stock reduction and reservation queues.
        - Processing book returns.
        - Assigning books automatically to users in reservation queues.
        - Synchronizing changes across books.json and books_ordered.json.

    All operations use JSON files for persistence.
    """
    
    def loan(self, isbn, document):
        """
        Processes a loan request.

        If the book has available stock, a new loan is registered and added
        to the user's history with a timestamp. Stock is reduced by 1.

        If the book has no stock, the user is added to the reservation queue
        (unless already inside).

        Args:
            ISBN code of the book being borrowed.
            Document ID of the user borrowing the book.

        Returns: None
            
        """
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
        
        # Case: stock available → loan is granted
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

        # Case: no stock → add to reservation queue
        else:
            if document not in found_book['reservations']:
                found_book['reservations'].append(document) 
            else:
                print("This user is already in reservations.")
                
        # Save general books.json
        with open("data/books.json", "w") as file:
            json.dump(list_books, file, indent=4)
        
        # Save user changes
        with open("data/users.json", "w") as file:
            json.dump(list_users, file, indent=4)
            
        # Update ordered list
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
        """
        Processes a book return using Binary Search on books_ordered.json.

        Steps:
            1. Load the ordered book list.
            2. Perform Binary Search to find the returning book.
            3. If reservations exist:
                - Assign the book automatically to the next user in line (FIFO).
                - Register the loan in that user's history.
            4. If no reservations:
                - Increase stock by 1.
            5. Synchronize ALL changes across:
                - books_ordered.json
                - users.json
                - books.json

        Args: ISBN code of the book being returned.
            
        Returns: None
            
        """
        
        list_ordered = []
        
        with open("data/books_ordered.json", "r") as file:
            list_ordered = json.load(file)
        

        # Load users
        list_users = []
        with open("data/users.json", "r") as file:
            list_users = json.load(file)

        found_book = None
        low = 0
        high = len(list_ordered) - 1
        
        while low <= high:
            mid = (low + high) // 2
            mid_book = list_ordered[mid]
            
            if mid_book['isbn'] == isbn:
                found_book = mid_book
                break
            elif mid_book['isbn'] < isbn:
                low = mid + 1
            else:
                high = mid - 1
        
        if found_book is None:
            return print(f"The book with ISBN code: {isbn} does not exists")


        if len(found_book['reservations']) > 0:
            print("The book has reservations at this moment")
            
            next_user_doc = found_book['reservations'].pop(0)

            found_user = None
            for user in list_users:
                if user['document'] == next_user_doc:
                    found_user = user
                    break
            
            if found_user:
                now = datetime.datetime.now()
                date_str = now.strftime("%Y-%m-%d %H:%M:%S")
                
                loan_data = {
                    "isbn": found_book['isbn'],
                    "title": found_book['title'],
                    "document": found_user['document'],
                    "date": date_str
                }
                
                found_user['history'].append(loan_data)
                print(f"Book loaned to: {found_user['name']}")
        
        else:
            print("No reservations")
            found_book['stock'] += 1

        
        # Save ordered list
        with open("data/books_ordered.json", "w") as file:
            json.dump(list_ordered, file, indent=4)
            
        # Save updated users
        with open("data/users.json", "w") as file:
            json.dump(list_users, file, indent=4)
            
        # Synchronize with normal list
        with open("data/books.json", "r") as file:
            list_normal = json.load(file)
            
        for b in list_normal:
            if b['isbn'] == isbn:
                b['stock'] = found_book['stock']
                b['reservations'] = found_book['reservations']
                break
                
        with open("data/books.json", "w") as file:
            json.dump(list_normal, file, indent=4)
            
        print("Booked returned")     
