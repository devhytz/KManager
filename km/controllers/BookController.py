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

        Returns: True if the file exists or after creating it.
        """
        # Define the path to the file
        route = Path("data/books.json")
        
        # Check if the file exists
        if route.is_file():
            return True
        else:
            # If it doesn't exist, print a message and create it with an empty list
            print("File does not exist... creating.")
            empty_list = []
            with open("data/books.json", "w") as file:
                json.dump(empty_list, file, indent=4) # Create the file with JSON format

    
    def searching(self, isbn):
        """
        Performs a linear search in books.json to check if a book exists.

        Args: isbn (str): ISBN code to search for.
            
        Returns: bool: True if the book exists, False otherwise.
        """
        book_list = []
        # Load the list of books from the JSON file
        with open("data/books.json", "r") as file:
            book_list = json.load(file)
            
        # Iterate over the list to find an ISBN match
        for book in book_list:
            if book['isbn'] == isbn:
                return True # Return True if the ISBN is found
            
        return False # Return False if the loop finishes without finding it
        
    
    def order_book(self, book_list, new_book_dict):
        """
        Inserts a book into an already ordered list using an insertion approach.
        Books are ordered by their ISBN field (Insertion Sort method).

        Args:
            book_list (list): Existing ordered list.
            new_book_dict (dict): New book to insert.

        Returns:
            list: Updated ordered list.
        """
        new_isbn = new_book_dict['isbn']
        inserted = False
        
        # Iterate to find the correct insertion position
        for i in range(len(book_list)):
            # If the new ISBN is smaller than the current ISBN, insert it here
            if new_isbn < book_list[i]['isbn']:
                book_list.insert(i, new_book_dict)
                inserted = True
                break
        
        # If it was not inserted (it's the largest ISBN), append it to the end
        if not inserted:
            book_list.append(new_book_dict)
            
        return book_list


    def add_book(self, new_book):
        """
        Adds a new book to the general inventory (books.json) and the 
        ordered inventory (books_ordered.json).

        Args:
            new_book (Book): Book object to insert.

        Returns:
            None
        """
        # 1. Verify the existence of the main file
        if self.verify_file():
        
            # 2. Verify the existence of the ordered file and create it if necessary
            route_ordered = Path("data/books_ordered.json")
            if not route_ordered.is_file():
                with open(route_ordered, "w") as file:
                    ordered_list = []
                    json.dump(ordered_list, file, indent=4)

            # 3. Check if the book already exists
            if self.searching(new_book.isbn):
                return print(f"The Book with ISBN {new_book.isbn} already exists.")
                
            # 4. Format the Book object into a dictionary
            formatted_book = {
                "isbn": new_book.isbn,
                "title": new_book.title,
                "author": new_book.author,
                "value": new_book.value,
                "weight": new_book.weight,
                "stock": new_book.stock,
                "reservations": []
            }
            
            # 5. Write to the general file (books.json)
            general_list = []
            with open("data/books.json", "r") as file:
                general_list = json.load(file)
                
            general_list.append(formatted_book)
            
            with open("data/books.json", "w") as file:
                json.dump(general_list, file, indent=4)
                
            # 6. Write to the ordered file (books_ordered.json)
            ordered_list = []
            with open(route_ordered, "r") as file:
                ordered_list = json.load(file)
            
            self.order_book(ordered_list, formatted_book) # Insert in order
            
            with open(route_ordered, "w") as file:
                json.dump(ordered_list, file, indent=4)
            
            return print(f"Book '{new_book.title}' added success.")
        
            
    def search_book(self, isbn):
        """
        Searches for a book using binary search in books_ordered.json.
        This function is efficient because it uses the ordered file.

        Args: ISBN code.
            
        Returns: True if the book exists and its information is printed.
        """
        if self.verify_file():
            # First check if it exists using the linear search method (searching)
            if self.searching(isbn):
                # If it exists, use binary search to get the full object
                found_book = self.binary_search(isbn)
                    
                if found_book:
                    print("This book already exists:\n")
                    # Print the book details
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
    
    def searching_title(self, search_title, index = 0, book_list = []):
        """
        Recursive linear search by exact title match.

        Args:
            search_title (str): Title to search.
            index (int): Recursion index (counter).
            book_list (list): Loaded book list.

        Returns: True if found, False otherwise.
        """
        # Load the list on the first call if it's empty
        if len(book_list) == 0:
            with open("data/books.json", "r") as file:
                book_list = json.load(file)

        # Base case 1: The index exceeds the list length
        if index >= len(book_list):
            print("Not founded book")
            return False

        # Base case 2: A match is found
        if book_list[index]['title'] == search_title:
            print(f"ISBN:   {book_list[index]['isbn']}") 
            print(f"Title: {book_list[index]['title']}")
            print(f"Author:  {book_list[index]['author']}") 
            return True
            
        # Recursive step: Call the function with the next index
        else:
            return self.searching_title(search_title, index + 1, book_list)
        
    def searching_author(self, author, index = 0, book_list = []):
        """
        Recursive linear search that prints all books by the same author.

        Args:
            author (str): Author name.
            index (int): Current recursion index.
            book_list (list): Cached list of books.

        Returns: None   
        """
        # Load the list if it's the first call
        if len(book_list) == 0:
            with open("data/books.json", "r") as file:
                book_list = json.load(file)

        # Base case: The index exceeds the list length
        if index >= len(book_list):
            return

        # If there is a match, print the book
        if book_list[index]['author'] == author:
            print(f"ISBN:   {book_list[index]['isbn']}") 
            print(f"Title: {book_list[index]['title']}")
            print(f"Author:  {book_list[index]['author']}") 
            print("")
            
        # Recursive step: Continue searching, even if a match was found
        self.searching_author(author, index + 1, book_list)
    
    def list_books(self):
        """
        Prints a formatted list of all books in books.json.

        Returns: None
        """
        if self.verify_file():
            book_list = []
            
            # Load the list of books
            with open("data/books.json", "r") as file:
                book_list = json.load(file)
                
            # Iterate and print the attributes of each book
            for book in book_list:
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

        Args: Book instance (ISBN required for search).
            
        Returns: None
        """
        # 1. Check if the book exists
        if self.searching(book.isbn):
            
            book_list = []
            
            # 2. Load the list of books
            with open("data/books.json", "r") as file:
                book_list = json.load(file)
            
            # 3. Find the book by ISBN in the list
            for b in book_list:
                if b['isbn'] == book.isbn:
                    
                    # 4. Show the update options menu
                    print("1) To change ISBN code")
                    print("2) To change title")
                    print("3) To change author")
                    print("4) To change value")
                    print("5) To change weight")
                    print("6) To change all")
                    option = int(input("Select an option: "))
                    
                    # 5. Update the fields based on the option
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
                        case 6: # Option to update all fields
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
                
                    # 6. Write the updated list back to the JSON file
                    with open("data/books.json", "w") as file:
                        json.dump(book_list, file, indent=4)
                    
                    break # Exit the loop once the book is updated
                
        else:
            return print(f"{book.title} does not exist")
    
    def delete_book(self, isbn):
        """
        Removes a book from books.json by ISBN.

        Args: ISBN code.
        
        Returns: None
        """
        if self.verify_file():
        
            book_list = []
            # Load the list of books
            with open("data/books.json", "r") as file:
                book_list = json.load(file)
                
            new_list = []
            # Create a new list excluding the book with the matching ISBN
            for book in book_list:
                if book['isbn'] != isbn:
                    new_list.append(book)
                
            # Overwrite the file with the new list without the deleted book
            with open("data/books.json", "w") as file:
                json.dump(new_list, file, indent=4)
                    
            return print(f"The book with ISBN code: {isbn} was deleted")
        

    def merge_sort(self, book_list):
        """
        Merge Sort Algorithm: Sorts the list of books by the 'value' attribute.
        It's a Divide and Conquer algorithm.

        Args: Unordered list of books.
            
        Returns: Sorted list.
        """
        # Base case of recursion: if the list has 0 or 1 element, it's already sorted
        if len(book_list) <= 1:
            return book_list
        
        # Divide the list into two halves
        middle = len(book_list) // 2
        left = book_list[:middle]
        right = book_list[middle:]
        
        # Recursively call merge_sort to sort the halves
        sorted_left = self.merge_sort(left)
        sorted_right = self.merge_sort(right)
        
        # Merge the sorted halves
        return self.merge(sorted_left, sorted_right)
    
    def merge(self, sorted_left, sorted_right):
        """
        Merge Sort helper function: Merges two sorted lists into one single sorted list.

        Args:
            sorted_left: Left sorted half.
            sorted_right: Right sorted half.

        Returns: Merged and ordered list.
        """
        merged_list = []
        
        i = 0 # Pointer for the left list
        j = 0 # Pointer for the right list
        
        # Compare elements from both lists and add the smallest to the merged list
        while i < len(sorted_left) and j < len(sorted_right):
            
            if sorted_left[i]['value'] < sorted_right[j]['value']:
                merged_list.append(sorted_left[i])
                i += 1
            else:
                merged_list.append(sorted_right[j])
                j += 1
        
        # Add the remaining elements from the left list
        while i < len(sorted_left):
            merged_list.append(sorted_left[i])
            i += 1
            
        # Add the remaining elements from the right list
        while j < len(sorted_right):
            merged_list.append(sorted_right[j])
            j += 1
        
        return merged_list
    
    def value_report(self):
        """
        Generates a complete inventory report sorted by book value
        using Merge Sort.
        Saves the result in value_report.json.

        Returns: None
        """
        book_list = []
        
        # Load the list of books
        with open("data/books.json", "r") as file:
            book_list = json.load(file)
            
        # Apply Merge Sort on the 'value' field
        report = self.merge_sort(book_list)
        
        # Save the sorted report to a new JSON file
        with open("data/value_report.json", "w") as file:
            json.dump(report, file, indent=4)
            
    def binary_search(self, isbn):
        """
        Binary Search.

        Searches for a book inside books_ordered.json using ISBN as the key.

        Args: ISBN code.
            
        Returns: The found book dictionary or None.
        """
        path = Path("data/books_ordered.json")
        
        # Check if the ordered file exists
        if not path.is_file():
            print("The ordered file does not exist.")
            return None

        # Load the ordered list of books
        with open(path, "r") as file:
            ordered_list = json.load(file)
            
        low = 0 # Starting index
        high = len(ordered_list) - 1 # Ending index
        
        # Binary search loop
        while low <= high:
            middle = (low + high) // 2  # Calculate the middle index
            middle_book = ordered_list[middle]
            
            # Compare the target ISBN with the ISBN of the middle book
            if middle_book['isbn'] == isbn:
                return middle_book # Book found
            
            elif middle_book['isbn'] < isbn:
                low = middle + 1  # Discard the lower 
            else:
                high = middle - 1  # Discard the upper  )
    
        return None # Book not found
    

    def efficient_shelving(self):
        """
        Backtracking Algorithm: Finds the optimal combination of books that maximizes
        total value without exceeding 8kg total weight.

        Unlike the brute-force version, this does not require choosing exactly 4 books.
        Any number of books (1–n) can form the optimal combination.
        """
        book_list = []

        # Load books
        with open("data/books.json", "r") as file:
            book_list = json.load(file)

        print("Searching...")

        # Backtracking call (replaces the old incorrect call)
        best_value, best_books = self.searching_combinations(book_list, 0, 0, [])

        # Print result
        if best_value == 0:
            print("No valid combination found.")
        else:
            print(f"Best Total Value: ${best_value}")
            for book in best_books:
                print(f" - {book['title']} (${book['value']})")
            print(f"Total Weight: {sum(b['weight'] for b in best_books)} kg")


    def searching_combinations(self, books, index, current_weight, current_list):
        """
        Correct Backtracking algorithm.

        Args:
            books (list): All books.
            index (int): Current index in the list.
            current_weight (float): Current total weight.
            current_list (list): Current selected books.

        Returns:
            tuple: (best_value, best_list)
        """

        # If weight exceeded → invalid branch
        if current_weight > 8:
            return 0, []

        # If end of list → evaluate this combination
        if index == len(books):
            total_value = sum(b["value"] for b in current_list)
            return total_value, current_list

        current_book = books[index]

        # Option 1: DO NOT include current book
        value_excluded, list_excluded = self.searching_combinations(
            books, index + 1, current_weight, current_list
        )

        # Option 2: INCLUDE current book (if weight allows)
        value_included, list_included = self.searching_combinations(
            books,
            index + 1,
            current_weight + current_book["weight"],
            current_list + [current_book]
        )

        # Return the better of the two branches
        if value_included > value_excluded:
            return value_included, list_included
        else:
            return value_excluded, list_excluded

        

    def inefficient_shelving(self):
        """
        Brute-Force Search: Finds ALL combinations of 4 books whose total 
        weight

        This algorithm uses 4 nested loops to iterate over all non-repeating combinations.
        """
        book_list = []
        
        # Load the list of books
        with open("data/books.json", "r") as file:
            book_list = json.load(file)
        
        found = 0
        
        if len(book_list) < 4:
            print("The list hast less than 4 books.")
            return
        
        # Four nested loops for all combinations 
        for i in range(len(book_list)):
            for j in range(i + 1, len(book_list)): 
                for k in range(j + 1, len(book_list)): 
                    for l in range(k + 1, len(book_list)): 
                        
                        b1 = book_list[i]
                        b2 = book_list[j]
                        b3 = book_list[k]
                        b4 = book_list[l]
                        
                        # Calculate the total weight of the combination
                        total_weight = b1['weight'] + b2['weight'] + b3['weight'] + b4['weight']
                        
                        # Check the condition of exceeding 8kg
                        if total_weight > 8.0:
                            found += 1
                            print(f" Combinations: {found}")
                            print(f"[{b1['title']}, {b2['title']}, {b3['title']}, {b4['title']}]")
                            print(f"Total Weight: {total_weight}")
                            
        if found == 0:
            print("Any combinations its over 8 kg") 
            
    def author_value(self, author, index=0, book_list=[]):
        """
        Stack-based Recursion: Computes the total value of all books by a given author.

        The summation is performed during the **"unwinding"** phase of recursion (post-recursion).

        Args:
            author: Target author.
            index: Recursion index.
            book_list: Cached book list.

        Returns: Total value of the author's collection.
        """
        # Load the list if it's the first call
        if len(book_list) == 0:
            with open("data/books.json", "r") as file:
                book_list = json.load(file)

        # Base case: Index exceeds the list 
        if index >= len(book_list):
            return 0

        current_value = 0
        # Get the current book's value if the author matches
        if book_list[index]['author'] == author:
            current_value = book_list[index]['value']

        # Recursive call (
        temp_total = self.author_value(author, index + 1, book_list)
        
        # Summation on the unwind: Current value + value from the recursive call
        total = current_value + temp_total

        # Print the final result only on the initial call 
        if index == 0:
            print(f"The value of the collection of {author} is: ${total}")

        return total
    
    def author_weight(self, author, index=0, book_list=[], current_weight=0.0, count=0):
        """
        Tail Recursion: Computes the average weight of all books written by a given author.

        The summation is performed during the **"folding"** phase by passing accumulators 
        (current_weight, count) to the recursive call.

        Args:
            author: Author name.
            index: Current recursion index.
            book_list: Cached list.
            current_weight (float): Accumulator for the total weight of matching books.
            count (int): Accumulator for the number of matching books.

        Returns: Average weight of the author's books.
        """
        # Load the list if it's the first call
        if len(book_list) == 0:
            with open("data/books.json", "r") as file:
                book_list = json.load(file)

        # Base case Index exceeds the list.
        if index >= len(book_list):
            if count == 0:
                print("Not books found")
                return 0.0
            
            average = current_weight / count
            print(f"The average weight of the collection of {author} is: {average} kg")
            return average

        # Update the accumulators if the author matches
        if book_list[index]['author'] == author:
            current_weight += book_list[index]['weight']
            count += 1

        # Accumulators are passed as arguments
        return self.author_weight(author, index + 1, book_list, current_weight, count)