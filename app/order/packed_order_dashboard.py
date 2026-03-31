from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
from app.billing.generate_bill import GenerateBill
from app.utilities.file_handler import FileHandler


class PackedOrderDashboard:

    def __init__(self):
        self.view_menu = ViewMenu()
        self.take_order = TakeOrder()
        self.logger = Logger().get_logger()
        self.generate_bill = GenerateBill()
        self.handler = FileHandler()
        self.menu_shown = False
        self.table_no = None
        self.order_type = None
        self.order_done = False 

        
    def show_dashboard(self):

        self.logger.info("Pcaked order Dashboard opened")

        while True:
            print("\n ==== PACKED ORDER DASHBOARD ====")
            print("1.Take Order")
            print("2.Generate Bill")
            print("3.Back")

            option = (input("Enter Choose your Option: "))

            if not option.isdigit():
                print("Invalid input")
                self.logger.warning(f"Invalid input in main dashboard:{option}")
                continue

            option = int(option)

            if option == 1:
               
                self.order_menu_dashboard()
                self.logger.info("Packed order payment done")
                    

            elif option == 2:
                
                self.generate_bill.generate_bill()
                self.order_done = False
              
            elif option == 3:
                self.logger.info("Returning to Staff Dashboard")
                break
                  
            else:
                print("Invalid Option")
                self.logger.warning(f"Invalid option selected in main dashboard:{option}")
                           

    def order_menu_dashboard(self):

        self.logger.info("Order Menu Dashboard opened")

        while True:
            print("\033[;34m ==== ORDER MENU DASHBOARD ====\033[0m")
            print("\033[;37m1.Show Food Menu")
            print("2.Add Order")
            print("3.Show All Orders")
            print("4.Back")

            option = (input("Enter choose your Option: "))
            
            if not option.isdigit():
                print("Invalid input")
                continue
            option = int(option)
 
            if option == 1:
                 
                 if self.menu_shown:
                    print("\033[1;33mMenu already displayed\033[0m")
                    self.logger.info("Menu already shown, skipping display")
                    continue

                 self.view_menu.show_menu()
                 self.menu_shown = True
                 self.logger.info("Food menu displayed")
                        
               
            elif option == 2:
             
               if not self.menu_shown:
                   print("pehle menu dikhye")
                   self.logger.warning("Use tried to order without viewing menu")
                   continue
               
               
            
               print("\nSelect Order Type: ")
               print("1. Dine-In:  (eat in restaurant)")
               print("2. Takeaway: (take food home)")

               choice = input("Enter Choice: ")

               if not choice.isdigit():
                    print("Invalid input")
                    continue
               choice = int(choice)

               if choice == 1:
                    
                    while True:

                        table = (input("Enter table number: "))
                        if not table.isdigit():
                             
                            print("\033[1;31mInvalid table number\033[0m")
                            continue

                        table = int(table)

                        bookings = self.handler.read_data("app/database/tables.json") or []

                        table_found = False

                        for booked in bookings:
                            if booked["table"] == table:
                                table_found = True
                                break
                        if not table_found:

                            print("\033[1;31m Table not booked! Please book table first\033[0m")
                            continue

                        self.order_type = "Dine-In"
                        self.table_no = table
        
                        print(f"Table {table} selected")
                        print("Selected: Dine-In ")
                        self.take_order.take_order(table)
                        self.order_done = True
                        break
                    
                    
               elif choice == 2:

                    self.order_type = "Takeway"
                    self.table_no = None
                    self.take_order.take_order()
                    self.order_done = True 


               else:
                    print("Invalid choice")
                    continue   
               print(f"Selected:{self.order_type}")
               self.logger.info("Order placed successfully") 
                
             
             
            elif option == 3:
                self.logger.info("Viewing all orders")
                self.show_all_orders() 
                    

            elif option == 4:
                self.logger.info("Return from packed order Dashboard")
                packed = PackedOrderDashboard()
                packed.show_dashboard()
                self.menu_shown = False
                break

                
            else:
                print("Invalid option")
                self.logger.warning(f"Invalid option in order menu: {option}")

    def show_all_orders(self):
                try:
                    orders = self.take_order.handler.read_data(self.take_order.file)

                    if not orders:
                        print("No orders found")
                        return

                    last_order = orders[-1]  

                    print("\n===== YOUR LATEST ORDER ======")

                    for item in last_order["items"]:

                        print(f"Item Name : {item['name']}")
                        print(f"Size      : {item['size'].capitalize()}")
                        print(f"Price     : {item['amount'] // item['qty']}")
                        print(f"Quantity  : {item['qty']}")
                        print("---------------------------")

                    
                    print("==============================")

                except Exception as e:
                    print("Error:", e)




