from app.logs.logger import Logger
import json
import os

logger = Logger().get_logger()

class FileHandler:

    def read_data(self,filepath):
        

        if not os.path.exists(filepath):
            logger.warning(f"file not found: {filepath}")
            
            return []

        try:
            with open(filepath,"r") as file:
                content = file.read().strip()

                if not content:
                    logger.info(f" Empty file: {filepath}")
                    return []
                
                data = json.loads(content)

                if not isinstance(data,list):
                    logger.warning(f"Invalid data formate in {filepath},excepted list")
                
                    return []
                
                logger.info(f"Data read successfully form {filepath}")
                return data

        except json.JSONDecodeError as e:
                logger.error(f"JSON Error in {filepath}: {e}")
                return []        
    

    def save_data(self,filepath,data):
            try:

                with open(filepath,"w") as file:
                                    
                    json.dump(data,file, indent = 4) 
                logger.info(f"Data sucessfully saved in {filepath}")

            except Exception as e:
                logger.error(f"Error saving data in {filepath}: {e}")
               
               
     
     