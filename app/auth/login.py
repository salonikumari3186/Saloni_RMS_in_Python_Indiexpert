from app.utilities.file_handler import FileHandler
from app.auth.signup import input_password
from app.logs.logger import Logger

class LoginSystem:

    def __init__(self):
        self.file = "app/database/users.json"
        self.file_handler = FileHandler()
        self.logger = Logger().get_logger()

    def login(self):
        try:
          self.logger.info("Login process started")

          print("\n" + "="*60)
          print("\033[1;35m               LOGIN MENU")
          print("\033[1;37m\n"+"="*60)

          email = input("\033[1;37mEnter a Email : ")
          password = input_password("Enter a Password : ")
      
          users = self.file_handler.read_data(self.file)
          
          
          if not users:
            print("\033[1;31m No users registered. please signup first.")
            self.logger.warning("Users file is empty or no users registred")
            return False
          
          
          for user in users:
                  
            if user.get("email") == email:
                    
              if user.get("password") != password:

                print("\033[1;31mIncorrect Password")
                self.logger.warning(f"Incorrect password attempt for email: {email}")
                return False
              

                      
              if user.get("status") != "active":
                print("User inactive")
                self.logger.warning(f"Inactive user login attempt: {email}")
                return False
                      
              print("\033[1;32m ✅ Login Successfull") 

              from app.dashboard.staff_dashboard import StaffDashboard
              StaffDashboard().show_dashboard()
              return True
         
            
          print("\033[1;31mUser not found,please signup first ")
          self.logger.warning(f"Login attempt with unregistered email: {email}")
          return False 
        
        except Exception as e:
          print("\033[1;31mSomething went wrong,please try again!")
          print("Error:",e)
          self.logger.error(f"Login error: {e}")
         
          return False


