from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.menu.add_menu import AddMenu
from app.menu.update_menu import UpdateMenu
from app.menu.delete_menu import DeleteMenu
from app.order.view_orders import ViewOrders
from app.reports.view_report import ViewReport
from app.users.user_management import UserManagement
from app.utilities.file_handler import FileHandler


class AdminDashboard:


    def __init__(self):
        self.take_order = TakeOrder()
        self.add_menu = AddMenu()
        self.update_menu = UpdateMenu()
        self.delete_menu = DeleteMenu()
        self.view_orders = ViewOrders()
        self.view_report = ViewReport()
        self.user_management = UserManagement()
        self.handler = FileHandler()
        self.logger = Logger().get_logger()
        
    
    def show_dashboard(self):

        self.logger.info("Admin Dashboard opened")

        while True:
            print("\033[1;37m"'-'*40)
            print("\033[1;34m<==== ADMIN DASHBOARD ====>")
            print("\033[1;35m1. Mangge User")
            print("2. Add Menu Item")
            print("3. Update Menu Item")
            print("4. Delete Menu Item")
            print("5. View Menu")
            print("6. View Orders")
            print("7. Reports")
            print("8. View Bill")
            print("9. Logout")
            print("\033[1;37m"'-'*40)

            option = (input("\033[1;34m Please Enter option : "))

            if not option.isdigit():
                print("Invalid input")
                self.logger.warning(f"Invalid input in admin dashboard: {option}")
                continue

            option = int(option)

            if option == 1:
                self.logger.info("Admin managing user")
                self.user_management.show_menu()
                
                
            elif option == 2:
                self.add_menu.add_item()
                self.logger.info("Admin added menu item")
               
               
            elif option == 3:
                self.update_menu.update_item()
                self.logger.info("Admin update menu item")

               
            elif option == 4: 
               
               self.delete_menu.delete_item()
               
               
            elif option == 5:
                
               view = ViewMenu()
               view.show_menu()
               self.logger.info("Admin viewed orders")
                

            elif option == 6:
                self.view_orders.show_orders()
                self.logger.info("Admin viewed order")

            elif option == 7:
                self.view_report.show_report()
                self.logger.info("Admin viewed reports")

            elif option == 8:
                self.view_bills()
                self.logger.info("Admin viewed bills")    

            elif option == 9:
                print("Logout successfull")
                self.logger.info("Admin looged out")
                break

            else:
                print("Invalid Option") 
                self.logger.warning(f"Invalid option selected in admin dashboard: {option}")

    def view_bills(self): 
        orders = self.handler.read_data("app/database/orders.json") or []

        if not orders:
            print("No bills found")
            return

        print("\n====== ALL BILLS ======")

        for order in orders:
            print(f"\nOrder ID: {order['order_id']}")
            print(f"Table   : {order.get('table', 'N/A')}")
            print(f"Total   : Rs{order['total']}")
            print(f"Status  : {order['status']}")
            print("----------------------") 

     
     
