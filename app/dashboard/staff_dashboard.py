from app.logs.logger import Logger
from app.order.packed_order_dashboard import PackedOrderDashboard
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.billing.generate_bill import GenerateBill
 
class StaffDashboard:

    def __init__(self):
        self.view_menu = ViewMenu()
        self.take_order = TakeOrder()
        self.generate_bill = GenerateBill()
        self.logger = Logger().get_logger()

    def show_dashboard(self):

        self.logger.info("Staff Dashboard opened")
        
        while True:
            print("\033[1;37m""-"*60)
            print(" "*18 +"\033[1;37m>>==> STAFF DASHBOARD <==<<")
            print("\033[1;37m""-"*60)

            print("\033[1;36m1.Book Table")
            print("2.Take Order")
            print("3.Advance Table Bokking")
            print("4.pacekd Order")
            print("5.Logout")
            print("\033[1;37m"+ "-"*60)

            option = (input("Enter your option(1-5): "))

            if not option.isdigit():
                print("Option must be only number")
                self.logger.warning(f"Invalid inpput in staff dashboard: {option}")
                continue

            option = int(option)

            if option == 1:
                print("Book Table boking")
                self.logger.info("Staff Selcted Book Table")
               
               
            elif option == 2:
                self.logger.info("Staff selected Take Order")
                #from app.order.packed_order_dashboard import PackedOrderDashboard\
                packed = PackedOrderDashboard()
                packed.show_dashboard()

            elif option == 3:
               
                print("Advance Bookin logic")
                self.logger.info("Staff selected Advance Booking")

            elif option == 4:
                self.logger.info("Staff selected Packed Order")
                packed = PackedOrderDashboard()
                packed.show_dashboard()

            elif option == 5:
                print("Logout sucessfull")
                self.logger.info("Staff logged out")
                break
            else:
                print("Invalid option")
                self.logger.warning(f"Invalid option in Staff dashboard: {option}")


