from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class DeleteMenu:
    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()


    def delete_item (self):
        try:
            self.logger.info("Delet menu process started:")

            menu = self.handler.read_data(self.file)

            item_id = input("Enter item ID to delete: ")

            if not item_id .isdigit():
                print("Invalid ID")
                self.logger.warning(f"Invalid ID entered: {item_id}")
                return
                
            item_id = int(item_id)

            new_menu = [item for item in menu if item["id"] != item_id]

            if len(menu) == len(new_menu):
                print("Item not found")
                self.logger.warning(f"Item not found for Delete: {item_id}")
                return
            
            self.handler.save_data(self.file,new_menu)

            print("✅ Item deleted successfully")
            self.logger.info(f"Menu item deleted successfully: ID {item_id}")
            
        except Exception as e:
            print("Something went wrong")
            self.logger.error(f"Error deleting menu item: {e}")    

