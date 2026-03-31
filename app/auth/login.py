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
          print("\033[1;35m                 LOGIN MENU")
          print("\033[1;37m\n"+"="*60)

          email = input("\033[1;37mEnter a Email : ")
          password = input_password("Enter a Password : ")
      
          users = self.file_handler.read_data(self.file)

          
          if not users :
            print("\033[1;31m No users registered. please signup first.")
            self.logger.warning("Users file is empty or no users registred")
            return False
          
          found = False
          
          for user in users:
                
                if user["email"] == email:
                  found = True

                  if user["password"] != password:
                      print("Incorrect Password")
                      self.logger.warning(f"Wrong password for {email}")
                      return False

                  if user["status"] != "active":
                      print("User inactive")
                      self.logger.warning(f"Inactive user login attempt: {email}")
                      return False

                  role = user.get("role")

                  if role == "admin":
                      print("Welcome Admin")
                      
                      self.logger.info(f"Admin logged in: {email}")
                      return "admin"

                    #   from app.dashboard.admin_dashboard import AdminDashboard
                    #   AdminDashboard().show_dashboard()
                    #   return True

                  elif role == "staff":
                      print("Welcome Staff")
                      self.logger.info(f"Staff logged in: {email}")

                      from app.dashboard.staff_dashboard import StaffDashboard
                      StaffDashboard().show_dashboard() 
                      return True

                  return True   
                

                if not found:
                    print("\033[1;31m User not found!please signup first\033[0m")
                    self.logger.warning(f"Login faliled,user not found: {email}")
                    return False 
           
        except Exception as e:
          print("\033[1;31mSomething went wrong,please try again!")
          print("Error:",e)
          self.logger.error(f"Login error: {e}")
         
          return False


