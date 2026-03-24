from app.auth.signup import SignupSystem
from app.auth.login import LoginSystem
from app.dashboard.admin_dashboard import AdminDashboard
from app.dashboard.staff_dashboard import StaffDashboard


Signup_system = SignupSystem()
login_system = LoginSystem()

admin_dashboard = AdminDashboard()
staff_dashboard = StaffDashboard()

def manage_user_menu():

    while True:
        print("\033[1;37m""\n" + "="*60)
        print("\t\033[1;33m <=== REGISTRATION MENU ===>")
        print("\033[1;37m"'='*60)
        print("\033[1;36m1.Signup")
        print("2.Login")
        print("3.Exit")
        print("\033[1;37m""="*60)

        option = (input("\033[;134mEnter your option:"))

        if not option.isdigit():
            print("\033[1;31moption must be only number!:")
            continue
        
        option = int(option)

        if option == 1:
            Signup_system.signup()

        elif option == 2:
            role= login_system.login()
            if role == "admin":
                print("\033[1;33m**** Welcome Admin ****")
                admin_dashboard.show_dashboard()

            elif role == "staff":
                print("\033[1;34m**** Welcome Staff ****")    

                print("\033[1;33mWelcome to Restaurant Management System")
                staff_dashboard.show_dashboard()        

        elif option == 3:
            print("EXIT !")
            break 

        else:
            print("\033[1;31mInvalid Option,Please select (1,2,3) option.")       