from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger


class UpdateMenu:
    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def update_item(self):

        try:
            self.logger.info("Update menu process started")

            menu = self.handler.read_data(self.file)

            item_id = input("Enter item ID to update: ")

            if not item_id.isdigit():
                print("Invalid ID")
                self.logger.warning(f"Invalid ID entered: {item_id}")
                return

            item_id = int(item_id)

            for item in menu:
                if item["id"] == item_id:

                    print(f"Updating: {item['name']}")
                    self.logger.info(f"Updating menu item: ID {item_id}")

                    new_name = input("New Name (Enter to skip): ")
                    new_half = input("New half price: ")
                    new_full = input("New full price: ")

                    if new_name:
                        item["name"] = new_name

                    if new_half.isdigit():
                        item["half_price"] = int(new_half)

                    if new_full.isdigit():
                        item["full_price"] = int(new_full)

                    self.handler.save_data(self.file, menu)

                    print("✅ Item updated successfully")
                    self.logger.info(f"Menu item updated successfully: ID {item_id}")
                    return

            print("Item not found")
            self.logger.warning(f"Item not found for update: {item_id}")

        except Exception as e:
            print("Something went wrong")
            self.logger.error(f"Error updating menu item: {e}")

      
      