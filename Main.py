import tkinter as tk
from tkinter import simpledialog, messagebox

from km.controllers.BookController import BookController
from km.controllers.UserController import UserController
from km.controllers.LoanController import LoanController
from km.models.Book import Book
from km.models.User import User
import json
import io
import sys


books = BookController()
users = UserController()
loans = LoanController()


def add_book():
    
    try:
        isbn = simpledialog.askstring("ISBN", "Enter ISBN:")
        title = simpledialog.askstring("Title", "Enter the title:")
        author = simpledialog.askstring("Author", "Enter the author:")
        value = int(simpledialog.askstring("Value", "Enter the value (number):"))
        weight = float(simpledialog.askstring("Weight", "Enter the weight (kg):"))
        stock = int(simpledialog.askstring("Stock", "Enter the stock:"))

        new_book = Book(isbn, title, author, value, weight, stock)
        books.add_book(new_book)
        messagebox.showinfo("OK", "Book added successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_user():
    
    try:
        doc = simpledialog.askstring("Document", "Enter the document number:")
        name = simpledialog.askstring("Name", "Enter the name:")

        new_user = User(doc, name)
        users.add_user(new_user)
        messagebox.showinfo("Ok", "User added successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def make_loan():
    isbn = simpledialog.askstring("Loan", "Enter the ISBN:")
    doc = simpledialog.askstring("Loan", "Enter the user document:")
    try:
        loans.loan(isbn, doc)
        messagebox.showinfo("OK", "Loan processed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def return_book():
    isbn = simpledialog.askstring("Return", "Enter the ISBN of the book to return:")
    try:
        loans.return_book(isbn)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def list_books():
 
    try:
        with open("data/books.json", "r") as f:
            lst = json.load(f)
        msg = "\n".join([f"{b['title']} - {b['author']} (ISBN {b['isbn']})" for b in lst])
        messagebox.showinfo("Books", msg if msg else "No books available.")
    except:
        messagebox.showerror("Error", "Could not read books.json")


def list_users():
    import json
    try:
        with open("data/users.json", "r") as f:
            lst = json.load(f)
        msg = "\n".join([f"{u['name']} ({u['document']})" for u in lst])
        messagebox.showinfo("Users", msg if msg else "No users available.")
    except:
        messagebox.showerror("Error", "Could not read users.json")


def search_book_isbn():
    isbn = simpledialog.askstring("Search ISBN", "Enter the ISBN:")
    if isbn is None:
        return
    
    found = books.searching(isbn) 
    if not found:
        messagebox.showwarning("Not found", f"No book with ISBN {isbn}")
        return
    
    book = books.binary_search(isbn)  
    
    msg = (
        f"ISBN: {book['isbn']}\n"
        f"Title: {book['title']}\n"
        f"Author: {book['author']}\n"
        f"Value: {book['value']}\n"
        f"Weight: {book['weight']}\n"
        f"Stock: {book['stock']}\n"
        f"Reservations: {book['reservations']}"
    )
    
    messagebox.showinfo("Book Found", msg)



def search_title():
    title = simpledialog.askstring("Search by Title", "Enter the exact title:")
    if title is None:
        return
    
    import json
    try:
        with open("data/books.json", "r") as f:
            books_list = json.load(f)
    except:
        messagebox.showerror("Error", "Could not read books.json")
        return

    for b in books_list:
        if b["title"] == title:
            msg = (
                f"ISBN: {b['isbn']}\n"
                f"Title: {b['title']}\n"
                f"Author: {b['author']}\n"
                f"Value: {b['value']}\n"
                f"Weight: {b['weight']}\n"
                f"Stock: {b['stock']}\n"
                f"Reservations: {b['reservations']}"
            )
            messagebox.showinfo("Book Found", msg)
            return
    
    messagebox.showwarning("Not Found", f"No book with title '{title}'")



def search_author():
    author = simpledialog.askstring("Search by Author", "Enter the author's name:")
    if author is None:
        return

    import json
    try:
        with open("data/books.json", "r") as f:
            books_list = json.load(f)
    except:
        messagebox.showerror("Error", "Could not read books.json")
        return

    matches = []
    for b in books_list:
        if b["author"] == author:
            matches.append(
                f"Title: {b['title']}\n"
                f"ISBN: {b['isbn']}\n"
                f"Value: {b['value']}\n"
                f"Weight: {b['weight']}\n"
                f"Stock: {b['stock']}\n"
                f"Reservations: {b['reservations']}\n"
                "---------------------------"
            )

    if not matches:
        messagebox.showwarning("Not Found", f"No books found for author '{author}'")
    else:
        msg = "\n".join(matches)
        messagebox.showinfo(f"Books by {author}", msg)
        
def generate_value_report():
    try:
        books.value_report()

        with open("data/value_report.json", "r") as file:
            report = json.load(file)

        if len(report) == 0:
            text = "No books available."
        else:
            text = "\n".join([
                f"{b['title']}  |  Value: ${b['value']}  |  ISBN: {b['isbn']}"
                for b in report
            ])

        report_window = tk.Toplevel(root)
        report_window.title("Value Report (Merge Sort)")
        report_window.geometry("450x400")

        tk.Label(report_window, text="Books Ordered by Value", font=("Arial", 14)).pack(pady=10)

        text_area = tk.Text(report_window, wrap="word", width=50, height=20)
        text_area.pack(padx=10, pady=10)

        text_area.insert("1.0", text)
        text_area.config(state="disabled")

        messagebox.showinfo("Report", "Value report generated successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        
def show_inefficient_shelving():
    try:     

        buffer = io.StringIO()
        sys.stdout = buffer 

        books.inefficient_shelving()  

        sys.stdout = sys.__stdout__ 

        output = buffer.getvalue()

        if output.strip() == "":
            output = "No combinations found."

        win = tk.Toplevel(root)
        win.title("Shelf Risk Report (Brute Force)")
        win.geometry("500x500")

        tk.Label(win, text="Brute Force Shelf Analysis", font=("Arial", 14)).pack(pady=10)

        text_area = tk.Text(win, wrap="word", width=60, height=25)
        text_area.pack(padx=10, pady=10)

        text_area.insert("1.0", output)
        text_area.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))
def show_efficient_shelving():
    try:
        import json
        import io
        import sys

        buffer = io.StringIO()
        sys.stdout = buffer 

        books.efficient_shelving() 

        sys.stdout = sys.__stdout__ 

        output = buffer.getvalue()

        if output.strip() == "":
            output = "No optimal combination found."

        # Crear ventana
        win = tk.Toplevel(root)
        win.title("Optimal Shelf Report (Backtracking)")
        win.geometry("500x500")

        tk.Label(win, text="Optimal Shelf Configuration", font=("Arial", 14)).pack(pady=10)

        text_area = tk.Text(win, wrap="word", width=60, height=25)
        text_area.pack(padx=10, pady=10)

        text_area.insert("1.0", output)
        text_area.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_all_shelves():
   

   
    backup_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        books.inefficient_shelving()  
        

        result = sys.stdout.getvalue()

        if result.strip() == "":
            result = "No se encontraron combinaciones."

        top = tk.Toplevel()
        top.title("All Shelving Combinations")
        top.geometry("600x500")

        text_box = tk.Text(top, wrap="word")
        text_box.insert("1.0", result)
        text_box.pack(expand=True, fill="both")

    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        sys.stdout = backup_stdout



root = tk.Tk()
root.title("Book Manger")
root.geometry("300x450")

tk.Label(root, text="Book Manager", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Add book", width=25, command=add_book).pack(pady=5)
tk.Button(root, text="Add user", width=25, command=add_user).pack(pady=5)

tk.Button(root, text="Loan book", width=25, command=make_loan).pack(pady=5)
tk.Button(root, text="Return book", width=25, command=return_book).pack(pady=5)

tk.Button(root, text="Search ISBN", width=25, command=search_book_isbn).pack(pady=5)
tk.Button(root, text="Seach title", width=25, command=search_title).pack(pady=5)
tk.Button(root, text="Search Auhtor", width=25, command=search_author).pack(pady=5)

tk.Button(root, text="All books", width=25, command=list_books).pack(pady=5)
tk.Button(root, text="All users", width=25, command=list_users).pack(pady=5)

tk.Button(root, text="Value Report (Merge Sort)", width=25, command=generate_value_report).pack(pady=5)
tk.Button(root, text="Shelf Risk (Brute Force)", width=25, command=show_inefficient_shelving).pack(pady=5)
tk.Button(root, text="Shelf Optimization (Backtracking)", width=25, command=show_efficient_shelving).pack(pady=5)
tk.Button(root, text="All Shelving Combinations", width=25, command=show_all_shelves).pack(pady=5)



root.mainloop()
