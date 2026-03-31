from app.logs.logger import Logger
from app.order.packed_order_dashboard import PackedOrderDashboard
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.billing.generate_bill import GenerateBill
from app.tablebooking.table_booking import TableBooking
 
class StaffDashboard:

    def __init__(self):
        
        self.view_menu = ViewMenu()
        self.take_order = TakeOrder()
        self.generate_bill = GenerateBill()
        self.table_booking = TableBooking()
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
                self.table_booking.book_table()
                self.logger.info("Staff Selcted Book Table")
               
               
            elif option == 2:
                self.logger.info("Staff selected Dine-In Order")

                packed = PackedOrderDashboard()
                packed.order_menu_dashboard()
               

            elif option == 3:
               
                self.logger.info("Staff selected Advance Table Booking")
                try:
                    self.table_booking.advance_booking()

                except Exception as e:
                    print("❌ Error while advance booking")
                    self.logger.error(f"Error in advance booking from staff dashboard: {e}")    
                

            elif option == 4:

                packed= PackedOrderDashboard()
                packed.show_dashboard()
               
          
            elif option == 5:
                print("Logout sucessfull")
                self.logger.info("Staff logged out")
                break
            else:
                print("Invalid option")
                self.logger.warning(f"Invalid option in Staff dashboard: {option}")


