from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class AddMenu:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()


    def add_item(self):

        try:
            self.logger.info ("Add menu process started")

            menu = self.handler.read_data(self.file)

            name = input("\033[1;37mEnter item name:")

            category=("\033[1;34m.Enter Category(Starters/Main Course/Rice & Biryani/Sweets/Drinks)")

            item_type = input("Type (Starters/Veg/Non-Veg/Drinks/Fastfood):")
        
            half = input("Enter half price: ")
            full = input("Enter full price: ")

            if not half.isdigit() or not full.isdigit():
                print("Price must be number")
                self.logger.warning("Invalid price entered:")
                return
            
            new_id = max([item["id"]for item in menu], default = 0)+1

            menu.append({
                "id":new_id,
                "name":name,
                "category":category,
                "type":item_type,
                "half_price":int(half),
                "full_price":int(full)
            })
            self.handler.save_data(self.file,menu)
            print("✅ Item added successfully")
            self.logger.info(f"Menu item added: {name} (ID: {new_id})")

        except Exception as e:
            print("Something want worng")
            self.logger.error(f"Error adding menu item: {e}")     
            

