from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger
import msvcrt
import uuid


def input_password(prompt = "\033[1;37mEnter Password:"):
    print(prompt, end ="",flush = True)
    password = ""

    while True:
        char = msvcrt.getch().decode("utf-8")

        if char == "\r":
            print()
            break
        elif char == "\b":
            if len(password) > 0:
                password = password [:-1]
                print("\b \b", end = "",flush = True)
        else:
            password += char
            print("*",end = "",flush =True)

    return password                  
    

class SignupSystem:
    

    def __init__(self):
        self.file = "app/database/users.json"
        self.file_handler = FileHandler()
        self.logger = Logger().get_logger()
    

    def signup(self):
    
        try:
            self.logger.info("Signup process started")

            while True:
                print("\n" +"="*60)

                print("\t\033[1;35m               SIGNUP MENU ")
                print("\n\033[1;37m" +"="*60)

                username = input("\033[1;37mEnter Username  : ").strip()

                if not username.isalpha():
                    print("\033[1;31mUsrename must be only char!")
                    self.logger.warning("Invalid username (non-alpha)")

                elif len(username) < 4:
                    print("\033[1;31mUsername must be 4 char!")
                    self.logger.warning("Username too short")
                else:
                    break 

            while True:   

                email = input("\033[1;37mEnter a Email  : ")

                if "@" not in email or ".com" not in email:
                    print("\033[1;31mInvalid Email")
                    self.logger.warning(f"Invalid email entered: {email}")
                else:
                    break

            while True:    

                password = input_password("\033[1;37mEnter a Password  : ")

                if len(password) < 6:
                    print("\033[1;31mpassword must be at least 6 char")
                    self.logger.warning("Password too short")

                else:
                    break

            while True:
                address = input("Enter Address  : ")
                if len(address.strip()) == 0:
                    print("\033[1;31mAddress cannot be empty")
                else:
                    break
                    
            

            role =  "staff"
                   
            users = self.file_handler.read_data(self.file)

            if not isinstance(users,list):
                    users = []
            exists = False

            for user in users:
                if user["username"] == username:
                    print("\033[1;31mUsername already exists")
                    self.logger.warning(f"Duplicate username attempt: {username}")
                    exists = True
                    break

            if exists:
                return

            user = {
                            
                "id":str(uuid.uuid4()),
                "username":username,
                "email":email,
                "password":password,
                "address":address,
                "role": role,
                "status":"active"
            } 
            users.append(user) 
            self.file_handler.save_data(self.file,users)
                            
            print("\033[1;32m✅ Signup Sucessfull")
            self.logger.info(f"New user registered: {username} ({email})")

        except Exception as e:
            print("\033[1;31msomethin went worng:",e)
            self.logger.error(f"Signup error: {e}")
                        

                
                
                    