from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger



class ViewMenu:

    def __init__(self):
        self.file = "app/database/menu.json"
        self.handler = FileHandler()
        self.logger = Logger().get_logger()

    def show_menu(self):
        try:
            self.logger.info("Loadinf menu data")
            COLORS = {
                "Starters":"\033[1;33m",
                "Main Course":"\033[1;32m",
                "Rice & Biryani":"\033[1;34m",
                "Sweets":"\033[1;35m",
                "Drinks":"\033[1;36m"
            }
            RESET = "\033[0m"
            
            menu = self.handler.read_data(self.file)
            
        
            if not menu:
                print("Menu is empty")
                return
        
            categories = {}

            for item in menu:
                category = item.get("category", "others")
                section = item.get("type", "Others")   

                categories.setdefault(category, {})
                categories[category].setdefault(section, []).append(item)


            width = 69 

            print("\n" + "|" + "="* width + "|")
            print("|\033[1;33m{:^60}\033[1;37m|".format("RESTAURANT MENU"))
            print("|" + "="* width+ "|")
        
            for category, sections in categories.items():
                color = COLORS.get(category,"\033[1;37m")

                print("\n" + "|" + "=" * width + "|")
                print(f"| {color}{category.upper():^{width-2}}{RESET} |")
                print("|" + "=" * width + "|")

        
                for section, items in sections.items():

                    section_color = "\033[1;32m" if section.lower() == "veg" else "\033[1;31m"

                    print(f"\n| {section_color}{section:<{width-2}}{RESET} |")
                    print("|" + "-" * width + "|")

                    # HEADER
                    print("| {:<4} {:<25} {:^16} {:^16} |".format(
                        "ID", "DISHES", "HALF PRICE", "FULL PRICE"
                    ))
                    print("|" + "-" * width + "|")

                    # ITEMS
                    for item in items:
                        print("| {:<4} {:<25} {:^16} {:^16} |".format(
                            item['id'],
                            item['name'],
                            item['half_price'],
                            item['full_price']
                        ))

                    print("|" + "-" * width + "|")
            self.logger.info("Menu displayed successfull") 
               
        except Exception as e:

            self.logger.error(f"Error displying menu: {e}")
            print("Something went worng while displyaing menu")            
            
            