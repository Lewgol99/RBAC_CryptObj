from colorama import Fore
import json

class AccessSubject:
    def extract_rbac_configuration(self):
        
        # Load Plaintext JSON Data Files
        with open('roles.json', 'r') as roles_file:
            self.roles_data = json.load(roles_file)
        
        with open('users.json', 'r') as users_file:
            self.users_data = json.load(users_file)

        with open('permissions.json', 'r') as permissions_file:
            self.permissions_data = json.load(permissions_file)
        
        print(Fore.LIGHTMAGENTA_EX + "All JSON files loaded Successfully!")
        return True
