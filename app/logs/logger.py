import logging
import os


class Logger:

    def __init__(self):
        log_folder = "app/logs"
        os.makedirs(log_folder, exist_ok=True)

        log_file = os.path.join(log_folder, "app.log")

        self.logger = logging.getLogger("RMS")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

    def get_logger(self):   
        return self.logger

    






    
     
    

       
       