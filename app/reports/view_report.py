from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger
from datetime import datetime

class ViewReport:


    def __init__(self):
        self.file = "app/database/orders.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def show_report(self):
        try:
            
            orders = self.handler.read_data(self.file)

            if not orders:
                print("No oreder found")
                return
            
            print("\n ====== REPORT MENU =====")
            print("1. All Report")
            print("2. Today Report")

            choice = input("Enter choice: ")

            if not choice.isdigit():
                print("Invalid input")
                return
            
            choice = int(choice)

            total_orders = len(orders)
            paid_orders = 0
            pending_orders = 0
            total_revenue = 0

            today = datetime.now().strftime("%Y-%m-%d")

            for order in orders:

            
                if choice == 2 and order.get("date") != today:
                    continue

                if order["status"] == "paid":
                    paid_orders += 1
                    total_revenue += order["total"]
                else:
                    pending_orders += 1

            print("\n====== REPORT ======")

            print(f"Total Orders   : {total_orders}")
            print(f"Paid Orders    : {paid_orders}")
            print(f"Pending Orders : {pending_orders}")
            print(f"Total Revenue  : Rs{total_revenue}")

            print("====================")

            self.logger.info("Report generated successfully")

        except Exception as e:
            print("\033[1;31mError generating report:\033[0m", e)
            self.logger.error(f"Report error: {e}")
           
           