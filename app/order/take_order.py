from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.menu.menu_manager import MenuManager
from app.utilities.file_handler import FileHandler
from datetime import datetime



class TakeOrder:

    def __init__(self):
        
        self.file = "app/database/orders.json"
        self.view_menu = ViewMenu()
        self.menu_manager = MenuManager()
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

        
    def take_order(self, table= None):

        self.logger.info("Order Process started")

        menu = self.menu_manager.load_menu()

        cart = []
        total = 0

        while True:

            if table is None:

                table_input= input("Enter table number: ").strip()

                if not table_input.isdigit():
                    print("\033[1;31m Invalid table number\033[0m")
                    continue

                table = int(table_input)
            else:
                if not isinstance(table,int):
                    print("Invalid table value")
                    return
                print(f"Taking order for table{table}")
                break

        while True:    
            try:
                item_id = int(input("\nEnter Fooditem ID: "))

                selected_item = None

                for item in menu:
                    if item["id"] == item_id:
                        selected_item = item
                        break

                if not selected_item:
                    print("Item not found")
                    continue

                size = input("Enter size(Half/Full): ").lower()

                if size == "half":
                    price = selected_item["half_price"]

                elif size == "full":
                    price = selected_item ["full_price"]

                else:
                    print("Invalid Size")
                    continue
                qty = int(input("Enter quantity: "))
                amount = price * qty

                cart.append({
                    "name": selected_item["name"],
                    "size": size,
                    "qty":  qty,
                    "amount": amount
                })    

                total += amount

                self.logger.info(f"Item added: {selected_item['name']} | Qty: {qty}")

                more = input("Add more item? (Yes/No)") 

                if more == "no":
                    break
                elif more != "yes":
                    print("Enter only yes or no")
                    continue

            except:
                    print("Invalid input")  
                    self.logger.warning("Invalid input during orders")
                    continue


        print("\n ==== ORDER SUMMARY ====")
        print("-"* 45)

        for item in cart:
            
            print(f"{item['name']} ({item['size']}) x{item['qty']} = Rs{item['amount']}")
            
            

        orders = self.handler.read_data(self.file) or []

        order_id = len(orders) + 1    

        orders.append({
            "order_id": order_id,
            "table": table,
            "items": cart,
            "total": total,
            "status": "pending",
            "date": datetime.now().strftime("%d-%m-%Y")
        })

        self.handler.save_data(self.file, orders)

        print("\n\033[1;32m✅ Order saved successfully!\033[0m")
        print("-"*45)
        self.logger.info(f"Order saved with ID: {order_id}")


                
                

