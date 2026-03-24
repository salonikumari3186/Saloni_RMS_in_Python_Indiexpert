from app.utilities.file_handler import FileHandler
from app.logs.logger import Logger


class MenuManager:

    def __init__(self):
        self.file ="app/database/menu.json"
        self.file_handler = FileHandler()
        self.logger = Logger().get_logger()

    def load_menu(self):
        try:
            menu = self.file_handler.read_data(self.file)
            self.logger.info("Menu loaded from file")
            return menu

        except  Exception as e:
            self.logger.error(f"Error loading menu: {e}")
            return []


        
    def save_menu(self,menu):
        try:
            self.file_handler.save_data(self.file,menu)    
            self.logger.info("Menu saved to file")
        
        except Exception as e:
            self.logger.error(f"Error saving menu: {e}")    