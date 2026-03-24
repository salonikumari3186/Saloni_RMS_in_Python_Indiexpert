from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.menu.add_menu import AddMenu
from app.menu.update_menu import UpdateMenu
from app.menu.delete_menu import DeleteMenu

class AdminDashboard:

    def __init__(self):
        self.take_order = TakeOrder()
        self.add_menu = AddMenu()
        self.update_menu = UpdateMenu()
        self.delete_menu = DeleteMenu()
        self.logger = Logger().get_logger()
    
    def show_dashboard(self):
        self.logger.info("Admin Dashboard opened")

        while True:
            print("\033[1;37m"'-'*40)
            print("\033[1;34m<==== ADMIN DASHBOARD ====>")
            print("\033[1;35m1.View Menu")
            print("2.Take Order")
            print("3.Add Menu Item")
            print("4.Udate Menu Item")
            print("5.Delete Menu Item")
            print("6.Logout")
            print("\033[1;37m"'-'*40)

            option = (input("\033[1;34mEnter option"))
            if not option.isdigit():
                print("Invalid input")
                self.logger.warning(f"Invalid input in admin dashboard: {option}")
                continue
            option = int(option)

            if option == 1:
                self.logger.info("Admin viewed menu")
                view = ViewMenu()
                view.show_menu()

            elif option == 2:
                self.logger.info("Admin viewed menu")
                self.take_order.take_order()

            elif option == 3:
                self.logger.info("Admin adding menu item")
                self.add_menu.add_item()

            elif option == 4:  
                self.logger.info("Admin deleting menu item")
                self.update_menu.update_item()

            elif option == 5:
                self.logger.info("Admin deleting menu item")
                self.delete_menu.delete_item()

            elif option == 6:

                self.logger.info("Admin logged out")
                break

            else:
                print("Invalid Option") 
                self.logger.warning(f"Invalid option selected in admin dashboard: {option}")  

