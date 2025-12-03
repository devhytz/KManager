from pathlib import Path
import json
from km.models.User import User

class UserController:
    """
    UserController

    This class manages all operations related to user handling inside the
    library system. It works with the persistent storage located in
    data/users.json and provides CRUD functionality.

    Responsibilities:
        - Create the users.json file if missing.
        - Add new users to the system.
        - Search for users by document ID.
        - List all registered users.
        - Update user information.
        - Delete users from the database.

    All functions maintain the JSON file updated so persistence is guaranteed
    without using external databases.
    """


    def verify_file(self):
        """
        Ensures that the users.json file exists.  
        If the file is missing, it is automatically created.

        Returns:
            bool: True if the file exists or was successfully created.
        """
        route = Path("data/users.json")

        if route.is_file():
            return True
        else:
            print("File does not exist... creating.")

            with open(route, "w") as file:
                json.dump([], file, indent=4)

            return True
    

    def searching(self, document):
        """
        Searches a user inside users.json by document number.

        Args:
            document (str): User document ID.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        with open("data/users.json", "r") as file:
            user_list = json.load(file)

        for user in user_list:
            if user["document"] == document:
                return True
        
        return False

    def add_user(self, new_user):
        """
        Adds a new user to the system.

        Args:
            new_user (User): Instance of User model containing user data.

        Returns:
            None
        """
        if self.verify_file():
            if not self.searching(new_user.document):

                with open("data/users.json", "r") as file:
                    list_users = json.load(file)

                formatted_user = {
                    "document": new_user.document,
                    "name": new_user.name,
                    "history": []
                }

                list_users.append(formatted_user)

                with open("data/users.json", "w") as file:
                    json.dump(list_users, file, indent=4)

                print(f"{formatted_user['name']} added")
            else:
                print(f"Error, {new_user.name} already exists.")

    
    def search_user(self, document):
        """
        Displays the information of a user searched by document.

        Args:
            document (str): User document ID.

        Returns:
            None
        """
        if self.verify_file():
            if self.searching(document):

                with open("data/users.json", "r") as file:
                    list_users = json.load(file)

                for user in list_users:
                    if user["document"] == document:
                        print("User found:\n")
                        print(f"Document: {user['document']}")
                        print(f"Name: {user['name']}")
                        print(f"History: {user['history']}")
                        return
            else:
                print(f"The user with document {document} does not exist.")

    
    def list_users(self):
        """
        Prints all users stored inside users.json.

        Returns:
            None
        """
        if self.verify_file():

            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            for user in list_users:
                print("")
                print(f"Document: {user['document']}")
                print(f"Name: {user['name']}")
                print("")

    
    def update_user(self, user):
        """
        Updates the attributes of an existing user.

        Args:
            user (User): User instance with the document to search for.

        Returns:
            None
        """
        if self.searching(user.document):

            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            for u in list_users:
                if u["document"] == user.document:

                    print("1) Change document")
                    print("2) Change name")
                    print("3) Change all")
                    option = int(input("Select an option: "))

                    match option:
                        case 1:
                            new_document = input("Enter new document: ")
                            u["document"] = new_document
                            print(f"Document updated to {new_document}")

                        case 2:
                            new_name = input("Enter new name: ")
                            u["name"] = new_name
                            print(f"Name updated to {new_name}")

                        case 3:
                            new_document = input("Enter new document: ")
                            u["document"] = new_document
                            print(f"Document updated to {new_document}")

                            new_name = input("Enter new name: ")
                            u["name"] = new_name
                            print(f"Name updated to {new_name}")

                            new_mail = input("Enter new mail: ")
                            u["mail"] = new_mail
                            print(f"Mail updated to {new_mail}")

                            print("\nSuccess\n")

                        case _:
                            print("Invalid option.")

                    with open("data/users.json", "w") as file:
                        json.dump(list_users, file, indent=4)

                    return
            
        else:
            print(f"{user.name} does not exist.")

    
    def delete_user(self, document):
        """
        Deletes a user from the system.

        Args:
            document (str): User document ID.

        Returns:
            None
        """
        if self.verify_file():

            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            new_list = [user for user in list_users if user["document"] != document]

            with open("data/users.json", "w") as file:
                json.dump(new_list, file, indent=4)

            print(f"The user with document {document} was deleted.")
