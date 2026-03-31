from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class UserManagement:

    def __init__(self):
        self.file = "app/database/users.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()
        #self.user_management = UserManagement()

    def show_menu(self):


        while True:
            print("\033[1;37m" +"-"*40)
            print("<===== USER MANAGEMENT =====>")
            print("\n" +"-"*40)
            print("1. View Users")
            print("2. Activate User")
            print("3. Deactivate User")
            print("4. Back")

            option = input("Enter option: ")

            if not option.isdigit():
                print("Invalid input")
                continue

            option = int(option)

            if option == 1:
                self.view_users()   

             
            elif option == 2:
                self.update_status("active")

            elif option == 3:
                self.update_status("inactive")

            elif option == 4:
                print("Returning to Admin Dashboard...")
                return  

            else:
                print("❌ Invalid choice")        

    def view_users(self):
        users = self.handler.read_data(self.file)

        if not users:
            print("No users found")
            return

        print("\n-------- USER LIST -------")

        for user in users:
            print(f"Name   : {user.get('username','No/Available')}")
            print(f"Email  : {user.get('email','No/Available')}")
            print(f"Role   : {user.get('role','No/Available')}")
            print(f"Status : {user.get('status','No/Available')}")
            print("-"*30)

        self.logger.info("Viewed all users") 

    def update_status(self, new_status):

        users = self.handler.read_data(self.file)

        if not users:
            print("No users found")
            return

        email = input("Enter user email: ")

        found = False

        for user in users:
            if user.get("email") == email:
                user["status"] = new_status
                found = True
                break

        if not found:
            print("❌ User not found")
            return

        self.handler.save_data(self.file, users)

        print(f"\033[1;33m✅ User {new_status} successfully")
        self.logger.info(f"User {email} set to {new_status}")     

    
          
            
