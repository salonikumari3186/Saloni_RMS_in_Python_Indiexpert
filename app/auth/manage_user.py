
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
        print("\n" + "="*60)
        print("\t<=== REGISTRATION MENU ===>")
        print("="*60)
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        print("="*60)

        option = input("Enter your option: ")

        if not option.isdigit():
            print("Option must be only number!")
            continue

        option = int(option)

        if option == 1:
            Signup_system.signup()

        elif option == 2:

            role = login_system.login()

            
            if not role:
                continue

            if role == "admin":
                #print("\033[1;33m**** Welcome Admin ****\033[0m")
                admin_dashboard.show_dashboard()
                return

            elif role == "staff":
                #print("\033[1;33m**** Welcome Staff ****\033[0m")
                staff_dashboard.show_dashboard()
                return

        elif option == 3:
            print("EXIT!")
            break

        else:
            print("Invalid Option, Please select (1,2,3)")