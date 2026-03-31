from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger

class AddMenu:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def add_item(self):

        try:
            self.logger.info("Add menu process started")

            menu = self.handler.read_data(self.file) or []

    
            name = input("\033[1;37mEnter item name: ").strip()

            if not name:
                print("\033[1;31m Name cannot be empty\033[0m")
                return

            if not name.replace(" ", "").isalpha():
                print("\033[1;31m Name must contain only alphabets\033[0m")
                return

            if len(name) < 3:
                print("\033[1;31m Name must be at least 3 characters\033[0m")
                return

        
            for item in menu:
                if item["name"].lower() == name.lower():
                    print("\033[1;31m Item already exists\033[0m")
                    return

            
            print("\nSelect Category:")
            print("1. Starters")
            print("2. Main Course")
            print("3. Rice & Biryani")
            print("4. Sweets")
            print("5. Fastfood")
            print("6. Drinks")

            categories = {
                "1": "Starters",
                "2": "Main Course",
                "3": "Rice & Biryani",
                "4": "Sweets",
                "5": "Fast Food",
                "6": "Drinks",
            }

            category_choice = input("Enter choice (1-6): ")

            if category_choice not in categories:
                print("\033[1;31m Invalid Category\033[0m")
                return

            category = categories[category_choice]

            print("\033[1;35mSelect Type:")
            print("1. Veg")
            print("2. Non-Veg")

            types = {
                "1": "Veg",
                "2": "Non-Veg"
            }

            type_choice = input("Enter choice (1-2): ")

            if type_choice not in types:
                print("\033[1;31m Invalid Type\033[0m")
                return

            item_type = types[type_choice]

            
            while True:
                half_price = input("Enter half price: ").strip()

                if not half_price.isdigit():
                    print("\033[1;31m Price must be number\033[0m")
                    continue

                half_price = int(half_price)

                if half_price <= 0:
                    print("\033[1;31m Price must be greater than 0\033[0m")
                    continue

                break

            
            while True:
                full_price = input("Enter full price: ").strip()

                if not full_price.isdigit():
                    print("\033[1;31m Price must be number\033[0m")
                    continue

                full_price = int(full_price)

                if full_price <= half_price:
                    print("\033[1;31m Full price must be greater than half price\033[0m")
                    continue

                break

            
            new_id = max([item.get("id", 0) for item in menu], default=0) + 1

            
            menu.append({
                "id": new_id,
                "name": name,
                "category": category,
                "type": item_type,
                "half_price": half_price,
                "full_price": full_price
            })

            self.handler.save_data(self.file, menu)

            print("\033[1;32m✅ Item added successfully\033[0m")
            self.logger.info(f"Menu item added: {name} (ID: {new_id})")

        except Exception as e:
            print("\033[1;31m Error:", e, "\033[0m")
            self.logger.error(f"Error adding menu item: {e}")
