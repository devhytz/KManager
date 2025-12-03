import tkinter as tk
from tkinter import simpledialog, messagebox

from km.controllers.BookController import BookController
from km.controllers.UserController import UserController
from km.controllers.LoanController import LoanController


books = BookController()
users = UserController()
loans = LoanController()


def add_book():
    from km.models.Book import Book

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
    from km.models.User import User

    try:
        doc = simpledialog.askstring("Document", "Enter the document number:")
        name = simpledialog.askstring("Name", "Enter the name:")

        new_user = User(doc, name)
        users.add_user(new_user)
        messagebox.showinfo("OK", "User added successfully.")

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
    import json
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
    books.search_book(isbn)


def search_title():
    title = simpledialog.askstring("Search by Title", "Enter the exact title:")
    if title is None:
        return
    books.searching_title(title)


def search_author():
    author = simpledialog.askstring("Search by Author", "Enter the author's name:")
    if author is None:
        return
    books.searching_author(author)


# -------------------------------------
# VENTANA PRINCIPAL
# -------------------------------------
root = tk.Tk()
root.title("Biblioteca - Simple Tkinter")
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

root.mainloop()
