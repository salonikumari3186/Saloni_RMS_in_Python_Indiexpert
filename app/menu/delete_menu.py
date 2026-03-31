from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class DeleteMenu:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def delete_item(self):

        try:
            menu = self.handler.read_data(self.file) or []

            if not menu:
                print("Menu is empty")
                return

            item_id = input("Enter item ID to delete: ")

            if not item_id.isdigit():
                print("Invalid ID")
                return

            item_id = int(item_id)

            for item in menu:
                if item["id"] == item_id:

                    confirm = input(f"Are you sure to delete '{item['name']}'? (yes/no): ")

                    if confirm.lower() != "yes":
                        print("Delete cancelled")
                        return

                    menu.remove(item)
                    self.handler.save_data(self.file, menu)

                    print("✅ Item deleted successfully")
                    self.logger.info(f"Item deleted: ID {item_id}")
                    return

            print("Item not found")

        except Exception as e:
            print("Error:", e)
            self.logger.error(f"Delete error: {e}")