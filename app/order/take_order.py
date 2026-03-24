from app.logs.logger import Logger
from app.menu.view_menu import ViewMenu
from app.menu.menu_manager import MenuManager
from app.utilities.file_handler import FileHandler


import json

class TakeOrder:

    def __init__(self):
        
        self.file = "app/database/orders.json"
        self.view_menu = ViewMenu()
        self.menu_manager = MenuManager()
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

        
    def take_order(self):

        self.logger.info("Order Process started")

        menu = self.menu_manager.load_menu()

        cart = []
        total = 0

        while True:
            try:
                item_id = int(input("\nEnter ID:"))
            except:
                print("Invalid ID")
                self.logger.warning("Invalid item ID enterd")
                continue

            selected_item = next((item for item in menu if item["id"] == item_id), None)

            if not selected_item:
                print("Item not found")
                self.logger.warning(f"Item not found for ID: {item_id}")
                continue

            size = input("Enter size (half/full): ").strip().lower()

            if size == "half":
                price = selected_item["half_price"]

            elif size == "full":
                price = selected_item["full_price"]
            else:
                print("Invalid size")
                self.logger.warning(f"Invalid size for {selected_item['name']}")
                continue

            try:
                qty = int(input("Enter quantity: "))
            except:
                print("Invalid quantity")
                self.logger.warning("Invalid quantity entered")
                continue

            amount = price * qty            

            cart.append({
                "name": selected_item["name"],
                "size": size,
                "qty": qty,
                "amount": amount
            })
            self.logger.info(f"Item added: {selected_item['name']} | Qty: {qty}")

            total += amount

            more = input("Add more item? (yes/no): ").strip().lower()
            if more != "yes":
                break

        print("\033[1;33m===== ORDER SUMMARY ======")

        for item in cart:
            print(f"\033[1;36m{item['name']}({item['size']}) x{item['qty']} = Rs{item['amount']}")

        print(f"\nTotal = Rs{total}")

        
        orders = self.handler.read_data(self.file)

        if not orders:
            orders = []

        order_id = len(orders) + 1

        orders.append({
            "order_id": order_id,
            "items": cart,
            "total": total,
            "status": "pending"
        })   

        self.handler.save_data(self.file, orders)

        print("\n✅ Order saved successfully!")

            
        
        