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
            create = []
            
            with open("data/users.json", "w") as file:
                json.dump(create, file, indent=4)      
    
    # ----------------------------------- CRUD --------------------------
    #"data/users.json" - Ruta archivo users.json
    
    
    def searching(self, user):

        # Lista en la cual se guardará el contenido del archivo
        user_list = []
            
        with open("data/users.json", "r") as file:
            user_list = json.load(file)
            
        # Recorrer la lista e identificar el documento de cada usuario para compararlo
        for u in user_list:
            if u['document'] == user.document:
                return True
                     
                
    def add_user(self, new_user):
        # Verificar si existe el archivo
        if self.verify_file():
            if not self.searching(new_user):
                list_users = []
                
                # Traer informacion desde el archivo hasta una variable
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)
                    
                # Pasarlo a formato json
                format = {
                    "document" : new_user.document,
                    "name" : new_user.name,
                    "mail" : new_user.mail
                }
                
                # Meter el nuevo usuario en la lista
                list_users.append(format)
                
                # Pasar la nueva lista con el usuario añadido al archivo
                with open("data/users.json", "w") as file:
                    json.dump(list_users, file, indent=4)  
                
                print(f"{format['name']} added")     
            else:
                return print(f"Error, {new_user.name} already exists.")
        else:
            return print("File does not exist... creating.")
        
             
    def search_user(self, document):
        
        if self.verify_file():
            # Traemos la informacion a la lista vacia
            list_users = []
            
            with open("data/users.json", "r") as file:
                list_users = json.load(file)
                
                for u in list_users:
                    if u['document'] == document:
                        print(f"The user with document {u['document']} exists")
                        return True
        else:
            return print("File does not exist... creating.")
            
   
    def list_users(self):
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
        if self.verify_file():
            # Lista en la cual traemos la informacion
            list_users = []
            
            # Verificamos si el usuario realmente existe en el archivo
            if self.searching(user):
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)
                
                # Recorremos hasta encontrar el usuario
                for u in list_users:
                    if u['document'] == user.document:
                        
                        # Preguntamos que dato(s) se desean actualizar
                        option = int(input("1) To change document | 2) To change name | 3) To change mail | 4) To change all: "))
                        
                        match option:
                            case 1:
                                new_document = input("Introduce the new document number: ")
                                u['document'] = new_document
                                print(f"{u['document']} updated")
                            case 2:
                                new_name = input("Introduce the new name: ")
                                u['name'] = self.setName(new_name)
                                print(f"{u['name']} updated")
                            case 3:
                                new_mail = input("Introduce the new mail: ")
                                u['mail'] = new_mail
                                print(f"{u['mail']} updated")
                            case 4:
                                new_document = input("Introduce the new document number: ")
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
        else:
            return print("File does not exist... creating.")                   
                        
            
    
            
    
       
        