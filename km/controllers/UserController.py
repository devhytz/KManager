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

        Returns: True if the file exists or was successfully created.

        """
        route = Path("data/users.json")

        if route.is_file():
            # The file is here, return True
            return True
        else:
            print("File does not exist... creating.")

            # Create the file and write an empty list inside to start
            with open(route, "w") as file:
                json.dump([], file, indent=4)

            # File is now ready
            return True


    def searching(self, document):
        """
        Searches a user inside users.json by document number.

        Args: document (str): User document ID.

        Returns: bool: True if the user exists, False otherwise.

        """
        # Open the file in read mode
        with open("data/users.json", "r") as file:
            user_list = json.load(file)

        # Loop through all users to find a match
        for user in user_list:
            if user["document"] == document:
                return True

        # No user found
        return False

    def add_user(self, new_user):
        """
        Adds a new user to the system.

        Args: new_user (User): Instance of User model containing user data.

        Returns: None

        """
        # First, ensure the file is ready
        if self.verify_file():
            # Check if the user document is NOT already in the system
            if not self.searching(new_user.document):

                # Read existing users from the JSON file
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)

                # Create the user dictionary with required fields
                formatted_user = {
                    "document": new_user.document,
                    "name": new_user.name,
                    "history": [] # User starts with an empty history
                }

                # Add the new user to the list
                list_users.append(formatted_user)

                # Write the complete list back to the file (save changes)
                with open("data/users.json", "w") as file:
                    json.dump(list_users, file, indent=4)

                print(f"{formatted_user['name']} added")
            else:
                # User already exists
                print(f"Error, {new_user.name} already exists.")


    def search_user(self, document):
        """
        Displays the information of a user searched by document.

        Args: document (str): User document ID.

        Returns: None
        """
        # Check if file exists and is ready
        if self.verify_file():
            # Check if the user is in the system
            if self.searching(document):

                # Load all users
                with open("data/users.json", "r") as file:
                    list_users = json.load(file)

                # Find and print the user's details
                for user in list_users:
                    if user["document"] == document:
                        print("User found:\n")
                        print(f"Document: {user['document']}")
                        print(f"Name: {user['name']}")
                        print(f"History: {user['history']}")
                        return # Stop searching after finding the user
            else:
                # User not found
                print(f"The user with document {document} does not exist.")


    def list_users(self):
        """
        Prints all users stored inside users.json.

        Returns: None

        """
        # Ensure the file is ready
        if self.verify_file():

            # Read all users from the file
            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            # Loop and print the information for each user
            for user in list_users:
                print("")
                print(f"Document: {user['document']}")
                print(f"Name: {user['name']}")
                print("")


    def update_user(self, user):
        """
        Updates the attributes of an existing user.

        Args: user (User): User instance with the document to search for.

        Returns: None

        """
        # Check if the user exists
        if self.searching(user.document):

            # Load all users from the file
            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            # Loop to find the user to update
            for u in list_users:
                if u["document"] == user.document:

                    # Show options to the user
                    print("1) Change document")
                    print("2) Change name")
                    print("3) Change all")
                    option = int(input("Select an option: "))

                    # Use match to handle options
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
                            # Update document
                            new_document = input("Enter new document: ")
                            u["document"] = new_document
                            print(f"Document updated to {new_document}")

                            # Update name
                            new_name = input("Enter new name: ")
                            u["name"] = new_name
                            print(f"Name updated to {new_name}")

                            print("Success")

                        case _:
                            print("Invalid option.")

                    # Save the updated list back to the file
                    with open("data/users.json", "w") as file:
                        json.dump(list_users, file, indent=4)

                    return # Stop after updating
        else:
            # User does not exist
            print(f"{user.name} does not exist.")


    def delete_user(self, document):
        """
        Deletes a user from the system.

        Args: document (str): User document ID.

        Returns: None

        """
        # Check if the file is ready
        if self.verify_file():

            # Load existing users
            with open("data/users.json", "r") as file:
                list_users = json.load(file)

            # Create a new list containing all users EXCEPT the one to delete
            new_list = [user for user in list_users if user["document"] != document]

            # Write the new list (without the deleted user) back to the file
            with open("data/users.json", "w") as file:
                json.dump(new_list, file, indent=4)

            print(f"The user with document {document} was deleted.")