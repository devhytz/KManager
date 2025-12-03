from km.models.User import User
from km.models.Book import Book
from km.controllers.UserController import UserController
from km.controllers.BookController import BookController
from km.controllers.LoanController import LoanController

import datetime


user_controller = UserController()
book_controller = BookController()
loan_controller = LoanController()

firstUser = User("1054862574", "Alejandro", "alejo70665@gmail.com")
secondUser = User("30338037", "Paulas", "paulita@gmail.com")



# controller.searching(secondUser) X
# controller.add_user(tirhtUser) FUNCIONANDO EXCELENTE
# controller.list_users() FUNCIONANDO EXCELENTE
# controller.update_user(tirhtUser) FUNCIONANDO EXCELENTE

# controller.search_user("105486254") FUNCIONANDO PERO FALTA EL ELSE EN CASO DE QUE NO SE ENCUENTRE

# book_controller.add_book(firstBook) FUNCIONANDO EXCELENTE
# book_controller.search_book("0123456789") FUNCIONANDO PERO FALTA EL ELSE EN CASO DE QUE NO SE ENCUENTRE
# book_controller.list_books() FUNCIONANDO EXCELENTE
# book_controller.update_book(firstBook) FUNCIONANDO EXCELENTE

#book_controller.add_book(secondBook)
#book_controller.delete_book("0123456789")

#book_controller.delete_book("8748484")#

#book_controller.search_book("1")
#user_controller.add_user(secondUser)
#user_controller.search_user("1054862574")
#user_controller.update_user(firstUser)

#book_controller.delete_book("0123456789")



#nuevo = Book("0123456789", "La Odisea", "Homero", 70000, 3, 1)
#otro = Book("1111111111", "La Biblia", "San Juan", 9000, 8, 1)
#book_controller.add_book(nuevo)
#loan_controller.loan("0123456789", "1054862574")
#loan_controller.return_book("0123456789")

#book_controller.value_report()
