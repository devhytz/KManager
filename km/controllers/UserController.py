from pathlib import Path
import json
from km.models.User import User

class UserController:
    """ DOC NO YET
    """
    
    # ------------------------ Auxiliar Methods -------------------------
    def verify_file(self):
        route = Path("data/users.json")
        
        if route.is_file():
            return True
        else:
            # Lista vacia
            print("File does not exist... creating.")
            create = []
            
            with open("data/users.json", "w") as file:
                json.dump(create, file, indent=4)      
    
    # ----------------------------------- CRUD --------------------------
    #"data/users.json" - Ruta archivo users.json
    
    def searching(self, document):

        # Lista en la cual se guardará el contenido del archivo
        user_list = []
            
        with open("data/users.json", "r") as file:
            user_list = json.load(file)
            
        # Recorrer la lista e identificar el documento de cada usuario para compararlo
        for user in user_list:
            if user['document'] == document:
                return True
                     
                
    def add_user(self, new_user):
        # Verificar si existe el archivo
        if self.verify_file():
            if not self.searching(new_user.document):
                
                list_users = []
                
                # Traer informacion desde el archivo hasta una variable
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)
                    
                # Pasarlo a formato json
                format = {
                    "document" : new_user.document,
                    "name" : new_user.name,
                    "mail" : new_user.mail,
                    "history" : []
                }
                
                # Meter el nuevo usuario en la lista
                list_users.append(format)
                
                # Pasar la nueva lista con el usuario añadido al archivo
                with open("data/users.json", "w") as file:
                    json.dump(list_users, file, indent=4)  
                
                print(f"{format['name']} added")     
            else:
                return print(f"Error, {new_user.name} already exists.")

        
             
    def search_user(self, document):
        
        if self.verify_file():
            if self.searching(document):
                # Traemos la informacion a la lista vacia
                
                list_users = []
                
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)
                    
                    for user in list_users:
                        if user['document'] == document:
                            print(f"This user already exists")
                            print("")
                            print(f"Document: {user['document']}")
                            print(f"Name: {user['name']}")
                            print(f"Mail: {user['mail']}")
                            print(f"History: {user['history']}")
                        return True
            else:
                return print(f"The user with document: {document} does not exists")
        
            
   
    def list_users(self):
        if self.verify_file():
        
            list_users = []
            
            with open("data/users.json", "r") as file:
                list_users = json.load(file)
                
            for user in list_users:
                
                # Imprime cada atributo para que se vea ordenado y los espacios por legibilidad
                print("")
                print(f"Document: {user['document']}")
                print(f"Name: {user['name']}")
                print(f"Mail: {user['mail']}")
                print("")
        
    
    def update_user(self, user):
        # Verificamos si el usuario realmente existe en el archivo
        
        
        if self.searching(user.document):
            
            # Lista en la cual traemos la informacion
            list_users = []
            
            with open("data/users.json", "r") as file:
                list_users = json.load(file)
            
            # Recorremos hasta encontrar el libro
            for u in list_users:
                if u['document'] == user.document:
                    
                    # Preguntamos que dato/s se desean actualizar
                    print("1) To change document")
                    print("2) To change name")
                    print("3) To change mail")
                    print("4) To change all")
                    option = int(input("Select an option: "))
                    
                    match option:
                        case 1:
                            new_document = input("Introduce the new document: ")
                            u['document'] = new_document
                            print(f"{u['document']} updated")
                        case 2:
                            new_name = input("Introduce the new name: ")
                            u['name'] = new_name
                            print(f"{u['name']} updated")
                        case 3:
                            new_mail = input("Introduce the new mail: ")
                            u['mail'] = new_mail
                            print(f"{u['mail']} updated")
                        case 4:
                            new_document = input("Introduce the new document: ")
                            u['document'] = new_document
                            print(f"{u['document']} updated")
                            
                            new_name = input("Introduce the new name: ")
                            u['name'] = new_name
                            print(f"{u['name']} updated")
                            
                            new_mail = input("Introduce the new mail: ")
                            u['mail'] = new_mail
                            print(f"{u['mail']} updated")
                            
                            print("")
                            print("Success")
                            print("")
                            
                        case _:
                            print("Invalid option")
                
                    # Enviamos la lista actualizada al archivo
                    with open("data/users.json", "w") as file:
                        json.dump(list_users, file, indent=4)
                    
                        
                    break
                
        else:
            return print(f"{user.name} does not exist")
            
    
    def delete_user(self, document):
        if self.verify_file():
        
                list_users = []
                
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)
                
                new_list = []
                
                for user in list_users:
                    if user['document'] != document:
                        new_list.append(user)
                
                with open("data/users.json", "w") as file:
                    json.dump(new_list, file, indent=4)
                    
                return print(f"The user with the document: {document} was deleted")
    
       
        