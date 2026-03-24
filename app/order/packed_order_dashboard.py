from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.order.take_order import TakeOrder
#from app.billing.generate_bill import GenerateBill


class PackedOrderDashboard:

    def __init__(self):
        self.view_menu = ViewMenu()
        self.take_order = TakeOrder()
        self.logger = Logger().get_logger()
       # self.generate_bill = GenerateBill()
        self.menu_shown = False
        
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
              

            elif option == 2:
               # self.generate_bill.generate_bill()
                print("biill")
                self.logger.info("Exited packed Order Dashboard")

            elif option == 3:
                self.logger.info("Exited packed Order Dashboard")
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
               
               self.take_order.take_order()
               self.logger.info("Take order function called")
                
            elif option == 3:
                self.logger.info("Viewing all orders")
                self.show_all_orders() 
                

            elif option == 4:
                self.logger.info("Exited Order Menu Dashboard")
                break
            else:
                print("Invalid option")
                self.logger.warning(f"Invalid option in order menu: {option}")

    def show_all_orders(self):

        try:

            orders = self.take_order.handler.read_data(self.take_order.file)

            if not orders:
                print("\033[1;31mNo orders found\033[10m")
                self.logger.info("No orders found in database")
                return
            
            print("\n\033[1;34m===== ALL ORDERS ======\033[0m")


            for order in orders:

                order_id = order.get("order_id")

                if not order_id:
                    self.logger.warning("Order without order_id found")
                    continue

                self.logger.info(f"Viewing Order ID: {order_id}")

                print(f"\n\033[1;36mOrder ID: {order_id}\033[0m")

                for item in order.get('items', []):
                    print(f"\033[1;32m{item['name']}({item.get('size')})\033[0m x{item['qty']} = \033[1;35mRs{item['amount']}\033[0m")

                print(f"\033[1;33mTotal: Rs{order.get('total', 0)}\033[0m")

                print("\00[1;37m"+"-"*40 + "\033[0m")

        except Exception as e:
            print("\033[1;31mSomething went wrong while showing orders\033[0m")
            self.logger.error(f"Error showing orders: {e}")
            