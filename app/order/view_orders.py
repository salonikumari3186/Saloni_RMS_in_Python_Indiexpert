from app.utilities.file_handler import FileHandler

class ViewOrders:

    def __init__(self):
        self.file = "app/database/orders.json"
        self.handler = FileHandler()

    def show_orders(self):
        orders = self.handler.read_data(self.file)

        if not orders:
            print("No orders found")
            return

        print("\033[1;34m ====== ALL ORDERS ======")
        for i, orders in enumerate(orders, start = 1):
            print(f"\nOrders {i}") 
            print("-"*30)

            for item in orders.get("items", []):
                print(f"{item['name']}({item['size']}) x{item['qty']} = Rs{item['amount']}")

            print("=" * 30)