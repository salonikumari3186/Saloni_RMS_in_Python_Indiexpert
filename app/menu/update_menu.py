from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class UpdateMenu:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def update_item(self):

        try:
            menu = self.handler.read_data(self.file) or []

            if not menu:
                print("Menu is empty")
                return

            item_id = input("Enter item ID to update: ")

            if not item_id.isdigit():
                print("Invalid ID")
                return

            item_id = int(item_id)

            item_found = None

            for item in menu:
                if item["id"] == item_id:
                    item_found = item
                    break

            if not item_found:
                print("Item not found")
                return

            print(f"\nUpdating Item: {item_found['name']}")

        
            name = input("Enter new name (leave blank to skip): ").strip()

            if name:
                if not name.replace(" ", "").isalpha():
                    print("Invalid name")
                    return

                
                for i in menu:
                    if i["name"].lower() == name.lower() and i["id"] != item_id:
                        print("Item already exists")
                        return

                item_found["name"] = name

            
            half_price = input("Enter new half price (leave blank to skip): ")

            if half_price:
                if not half_price.isdigit():
                    print("Invalid price")
                    return
                item_found["half_price"] = int(half_price)

            full_price = input("Enter new full price (leave blank to skip): ")

            if full_price:
                if not full_price.isdigit():
                    print("Invalid price")
                    return

                if int(full_price) <= item_found["half_price"]:
                    print("Full price must be greater than half price")
                    return

                item_found["full_price"] = int(full_price)

            self.handler.save_data(self.file, menu)

            print("✅ Item updated successfully")
            self.logger.info(f"Item updated: ID {item_id}")

        except Exception as e:
            print("Error:", e)
            self.logger.error(f"Update error: {e}")
