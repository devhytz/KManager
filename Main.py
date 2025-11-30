from km.models.User import User
from km.models.Book import Book
from km.models.Manager import Manager
from km.controllers.UserController import UserController
from km.controllers.BookController import BookController

import datetime


user_controller = UserController()
book_controller = BookController()

firstUser = User("1054862574", "Alejandro", "alejrios90@gmail.com", "alejo123")
secondUser = User("30338037", "Paulas", "paulita@gmail.com", "paulka13")
tirhtUser = User("74080282", "Orlando", "orlando@gmail.com", "orlando123")

firstBook = Book("0123456789", "Holahola", "Alejandro", 40000, 1.3)
secondBook = Book("987654321", "AdiosAdios", "Sergey", 2000, 7.3)

# controller.searching(secondUser) X
# controller.add_user(tirhtUser) FUNCIONANDO EXCELENTE
# controller.list_users() FUNCIONANDO EXCELENTE
# controller.update_user(tirhtUser) FUNCIONANDO EXCELENTE

# controller.search_user("105486254") FUNCIONANDO PERO FALTA EL ELSE EN CASO DE QUE NO SE ENCUENTRE

# book_controller.add_book(firstBook) FUNCIONANDO EXCELENTE
# book_controller.search_book("0123456789") FUNCIONANDO PERO FALTA EL ELSE EN CASO DE QUE NO SE ENCUENTRE
# book_controller.list_books() FUNCIONANDO EXCELENTE
# book_controller.update_book(firstBook) FUNCIONANDO EXCELENTE

#book_controller.add_book(firstBook)
book_controller.delete_book("0123456789")

#book_controller.delete_book("987654321")#

book_controller.search_book("1")