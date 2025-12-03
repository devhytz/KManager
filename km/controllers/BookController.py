from pathlib import Path
import json
from km.models.Book import Book

class BookController:
    """ 
    BookController

    This class manages the full lifecycle of books inside the library system.
    It provides CRUD operations, different searching algorithms, recursive 
    functions, a Merge Sort report generator, brute-force shelving detection,
    and an optimal shelving module using backtracking.

    All book information is stored in JSON files, keeping persistence 
    without a database.
    """
    
    
    def verify_file(self):
        """
        Verifies that the books.json file exists.  
        If it does not exist, the method automatically creates it.

        Returns:
            bool: True if the file exists or after creating it.
        """
        route = Path("data/books.json")
        
        if route.is_file():
            return True
        else:
            print("File does not exist... creating.")
            create = []
            with open("data/books.json", "w") as file:
                json.dump(create, file, indent=4)

    
    def searching(self, isbn):
        """
        Performs a linear search in books.json to determine if a book exists.

        Args:
            isbn (str): ISBN code to search for.

        Returns:
            bool: True if the book exists, False otherwise.
        """
        list_books = []
        with open("data/books.json", "r") as file:
            list_books = json.load(file)
            
        for book in list_books:
            if book['isbn'] == isbn:
                return True
              
                
    def order_book(self, list_books, new_book_dict):
        """
        Inserts a book into an already ordered list using an insertion-sort approach.
        Books are ordered by their ISBN field.

        Args:
            list_books (list): Existing ordered list.
            new_book_dict (dict): New book to insert.

        Returns:
            list: Updated ordered list.
        """
        isbn_new = new_book_dict['isbn']
        inserted = False
        
        for i in range(len(list_books)):
            if isbn_new < list_books[i]['isbn']:
                list_books.insert(i, new_book_dict)
                inserted = True
                break
        
        if not inserted:
            list_books.append(new_book_dict)
            
        return list_books


    def add_book(self, new_book):
        """
        Adds a new book to the general inventory (books.json) and the 
        ordered inventory (books_ordered.json).

        Args:
            new_book (Book): Book object to insert.

        Returns:
            None
        """
        if self.verify_file():
        
            route_ordered = Path("data/books_ordered.json")
            if not route_ordered.is_file():
                with open(route_ordered, "w") as file:
                    ordered_list = []
                    json.dump(ordered_list, file, indent=4)

            if self.searching(new_book.isbn):
                return print(f"The Book with ISBN {new_book.isbn} already exists.")
                
            format_book = {
                "isbn": new_book.isbn,
                "title": new_book.title,
                "author": new_book.author,
                "value": new_book.value,
                "weight": new_book.weight,
                "stock": new_book.stock,
                "reservations": []
            }
            
            list_general = []
            with open("data/books.json", "r") as file:
                list_general = json.load(file)
                
            list_general.append(format_book)
            
            with open("data/books.json", "w") as file:
                json.dump(list_general, file, indent=4)
                
            list_ordered = []
            with open(route_ordered, "r") as file:
                list_ordered = json.load(file)
            
            self.order_book(list_ordered, format_book)
            
            with open(route_ordered, "w") as file:
                json.dump(list_ordered, file, indent=4)
            
            return print(f"Book '{new_book.title}' added success.")
        
             
    def search_book(self, isbn):
        """
        Searches for a book using binary search in books_ordered.json.
        This function is critical for loan and reservation management.

        Args:
            isbn (str): ISBN code.

        Returns:
            bool: True if the book exists.
        """
        if self.verify_file():
            if self.searching(isbn):
                found_book = self.binary_search(isbn)
                    
                if found_book:
                    print("This book already exists:\n")
                    print(f"ISBN: {found_book['isbn']}")
                    print(f"Title: {found_book['title']}")
                    print(f"Author: {found_book['author']}")
                    print(f"Value: {found_book['value']}")
                    print(f"Weight: {found_book['weight']}")
                    print(f"Stock: {found_book['stock']}")
                    print(f"reservations: {found_book['reservations']}")
                    return True
            else:
                return print(f"The book with ISBN code: {isbn} does not exists.")
    
    def searching_title(self, searching, index = 0, list_books = []):
        """
        Recursive linear search by exact title match.

        Args:
            searching (str): Title to search.
            index (int): Recursion index.
            list_books (list): Loaded book list.

        Returns:
            bool: True if found, False otherwise.
        """
        if len(list_books) == 0:
            with open("data/books.json", "r") as file:
                list_books = json.load(file)

        if index >= len(list_books):
            print("Not founded book")
            return False

        if list_books[index]['title'] == searching:
            print(f"ISBN:   {list_books[index]['isbn']}") 
            print(f"Title: {list_books[index]['title']}")
            print(f"Author:  {list_books[index]['author']}") 
            return True
            
        else:
            return self.searching_title(searching, index + 1, list_books)
        
    def searching_author(self, author, index = 0, list_books = []):
        """
        Recursive linear search printing all books by the same author.

        Args:
            author (str): Author name.
            index (int): Current recursion index.
            list_books (list): Cached list of books.

        Returns:
            None
        """
        if len(list_books) == 0:
            with open("data/books.json", "r") as file:
                list_books = json.load(file)

        if index >= len(list_books):
            return

        if list_books[index]['author'] == author:
            print(f"ISBN:   {list_books[index]['isbn']}") 
            print(f"Title: {list_books[index]['title']}")
            print(f"Author:  {list_books[index]['author']}") 
            print("")
            
        self.searching_author(author, index + 1, list_books)
    
    def list_books(self):
        """
        Prints a formatted list of all books in books.json.

        Returns:
            None
        """
        if self.verify_file():
            list_books = []
            
            with open("data/books.json", "r") as file:
                list_books = json.load(file)
                
            for book in list_books:
                print("")
                print(f"ISBN: {book['isbn']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Value: {book['value']}")
                print(f"Weight: {book['weight']}")
                print("")
        
    
    def update_book(self, book):
        """
        Updates attributes of an existing book using a menu selection.

        Args:
            book (Book): Book instance (ISBN required).

        Returns:
            None
        """
        if self.searching(book.isbn):
            
            list_books = []
            
            with open("data/books.json", "r") as file:
                list_books = json.load(file)
            
            for b in list_books:
                if b['isbn'] == book.isbn:
                    
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
                
                    with open("data/books.json", "w") as file:
                        json.dump(list_books, file, indent=4)
                    
                    break
                
        else:
            return print(f"{book.title} does not exist")
    
    def delete_book(self, isbn):
        """
        Removes a book from books.json by ISBN.

        Args:
            isbn (str): ISBN code.

        Returns:
            None
        """
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
        

    def merge_sort(self, list):
        """
        Merge Sort (recursive)

        Sorts the list of books by the 'value' attribute.

        Args:
            list (list): Unordered list of books.

        Returns:
            list: Sorted list.
        """
        if len(list) <= 1:
            return list
        
        middle = len(list) // 2
        left = list[:middle]
        right = list[middle:]
        
        order_left = self.merge_sort(left)
        order_right = self.merge_sort(right)
        
        return self.merge(order_left, order_right)
    
    def merge(self, order_left, order_right):
        """
        Merges two sorted lists into one sorted list.

        Args:
            order_left (list): Left sorted half.
            order_right (list): Right sorted half.

        Returns:
            list: Merged ordered list.
        """
        order_list = []
        
        i = 0
        j = 0
        
        while i < len(order_left) and j < len(order_right):
            
            if order_left[i]['value'] < order_right[j]['value']:
                order_list.append(order_left[i])
                i += 1
            else:
                order_list.append(order_right[j])
                j += 1
        
        while i < len(order_left):
            order_list.append(order_left[i])
            i += 1
            
        while j < len(order_right):
            order_list.append(order_right[j])
            j += 1
        
        return order_list
    
    def value_report(self):
        """
        Generates a complete inventory report sorted by book value.
        Saves the result in value_report.json.

        Returns:
            None
        """
        list_books = []
        
        with open("data/books.json", "r") as file:
            list_books = json.load(file)
            
        report = self.merge_sort(list_books)
        
        with open("data/value_report.json", "w") as file:
            json.dump(report, file, indent=4)
            
    def binary_search(self, isbn):
        """
        Binary Search

        Searches for a book inside books_ordered.json using ISBN as key.

        Args:
            isbn (str): ISBN code.

        Returns:
            dict: Book found or None.
        """
        path = Path("data/books_ordered.json")
        
        if not path.is_file():
            print("El archivo ordenado no existe.")
            return None

        with open(path, "r") as file:
            ordered_list = json.load(file)
            
        low = 0
        high = len(ordered_list) - 1
        
        while low <= high:
            middle = (low + high) // 2      
            middle_book = ordered_list[middle]
            
            if middle_book['isbn'] == isbn:
                return middle_book
            
            elif middle_book['isbn'] < isbn:
                low = middle + 1   
            else:
                high = middle - 1   
    
        return None
    

    def optimizar_estanteria(self):
        """
        Backtracking algorithm to find the optimal combination of 4 books that:
        - Maximizes their total value.
        - Does not exceed 8kg total weight.

        Returns:
            None
        """
        lista_libros = []

        with open("data/books.json", "r") as archivo:
            lista_libros = json.load(archivo)
        
        print("Searching")
        
        mejor_valor, mejores_libros = self.buscar_combinacion(lista_libros, 8, 0, 4)

        if mejor_valor < 0:
            print("Not found a valid combination")
        else:
            print(f"Found Total Value: ${mejor_valor}")
            for libro in mejores_libros:
                print(f" - {libro['title']} (${libro['value']})")

    def buscar_combinacion(self, libros, espacio, indice, faltan):
        """
        Recursive Backtracking helper for optimal shelving.

        Args:
            libros (list): All books.
            espacio (float): Remaining weight.
            indice (int): Current index.
            faltan (int): Books still required.

        Returns:
            tuple: (best_value, best_combination)
        """
        if faltan == 0:
            return 0, []

        if espacio <= 0 or indice >= len(libros):
            return -999999, []

        libro = libros[indice]

        valor_no, lista_no = self.buscar_combinacion(libros, espacio, indice + 1, faltan)

        valor_si = -999999
        lista_si = []

        if libro['weight'] <= espacio:
            v_temp, l_temp = self.buscar_combinacion(libros, espacio - libro['weight'], indice + 1, faltan - 1)
            valor_si = v_temp + libro['value']
            lista_si = [libro] + l_temp

        if valor_si > valor_no:
            return valor_si, lista_si
        else:
            return valor_no, lista_no
        

    def inefficient_shelving(self):
        """
        Brute-force search for ALL combinations of 4 books whose total 
        weight exceeds 8kg.

        This algorithm checks all combinations (O(n^4)).

        Returns:
            None
        """
        list_books = []
        
        with open("data/books.json", "r") as file:
            list_books = json.load(file)
        
        found = 0
        
        if len(list_books) < 4:
            print("The list hast less than 4 books.")
            return
        
        for i in range(len(list_books)):              
            for j in range(i + 1, len(list_books)):   
                for k in range(j + 1, len(list_books)): 
                    for l in range(k + 1, len(list_books)): 
                        
                        l1 = list_books[i]
                        l2 = list_books[j]
                        l3 = list_books[k]
                        l4 = list_books[l]
                        
                        total_weight = l1['weight'] + l2['weight'] + l3['weight'] + l4['weight']
                        
                        if total_weight > 8.0:
                            found += 1
                            print(f" Combinations: {found}")
                            print(f"[{l1['title']}, {l2['title']}, {l3['title']}, {l4['title']}]")
                            print(f"Total Weight: {total_weight}")
                            
        if found == 0:
            print("Any combinations its over 8.0 kg")     
            
    def author_value(self, author, index=0, list_books=[]):
        """
        Recursive stack-based function that computes the total value of all
        books from a given author.

        The sum is performed during the "unwinding" phase of recursion.

        Args:
            author (str): Target author.
            index (int): Current recursion index.
            list_books (list): Cached book list.

        Returns:
            int: Total value of the author's collection.
        """
        if len(list_books) == 0:
            with open("data/books.json", "r") as file:
                list_books = json.load(file)

        if index >= len(list_books):
            return 0

        current_value = 0
        if list_books[index]['author'] == author:
            current_value = list_books[index]['value']

        total_temp = self.author_value(author, index + 1, list_books)
        
        total = current_value + total_temp

        if index == 0:
            print(f"The value of the collection of {author} is: ${total}")

        return total
    
    def author_weight(self, author, index=0, list_books=[], current_weight=0.0, count=0):
        """
        Tail recursion implementation that computes the average weight 
        of all books written by a given author.

        Args:
            author (str): Author name.
            index (int): Current recursion index.
            list_books (list): Cached list.
            current_weight (float): Accumulator of all matching weights.
            count (int): Number of matching books.

        Returns:
            float: Average weight of the author's books.
        """
        if len(list_books) == 0:
            with open("data/books.json", "r") as file:
                list_books = json.load(file)

        if index >= len(list_books):
            if count == 0:
                print("Not books found")
                return 0.0
            
            average = current_weight / count
            print(f"The average weight of the collection of {author} is: {average} kg")
            return average

        if list_books[index]['author'] == author:
            current_weight += list_books[index]['weight']
            count += 1

        return self.author_weight(author, index + 1, list_books, current_weight, count)
