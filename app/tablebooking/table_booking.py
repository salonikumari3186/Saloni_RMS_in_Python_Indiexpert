from app.utilities.file_handler import FileHandler
from datetime import datetime
from app.logs.logger import Logger


class TableBooking:

    def __init__(self):
        self.file = "app/database/tables.json"
        self.advance_file = "app/database/advance_tables.json"
        self.handler = FileHandler()
        self .total_tables = 10
        self.logger = Logger().get_logger()


    def book_table(self):
            
            try:
                
                self.logger.info("Table booking started")

                while True:

                    name = input("Enter Customer Name: ").strip()

                    if not name:
                        print("\033[1;31m Name cannot be empty\033[0m")
                        continue
                
                    if not name.replace(" ","").isalpha():
                        print("\033[1;31m Name must be contain only aplhabets\033[0m")
                        continue

                
                    if len(name) < 4:
                        print("\033[1;31m Name must be al least 4 charters long\033[0m")
                        continue

                    break  

                while True:    
                    
                    mobile = input("Enter Mobile Number: ").strip()

                    if not mobile.isdigit() or len(mobile)!= 10:
                        print(" Invalid mobile number is not exist (must be 10 digit)")
                        continue
                    break

                while True:

                    table = input("Enter Table Number: ").strip()

                    if not table.isdigit():
                        print("Invalid table must be numeric")
                        continue
                    table = int(table)

                    if table< 1 or table > self.total_tables:
                        print(f"\033[1;31m Only {self.total_tables} tables available\033[0m")
                        continue


                    persons = input("Number of Persons: ").strip()

                    if not persons.isdigit():
                        print("\033[1;31m Person must be a number\033[0m")
                        continue

                    persons = int(persons)

                    if persons <= 0:
                        print("\033[1;31m persons must be greater than 0\033[0m")
                        continue
                    break

                data = self.handler.read_data(self.file) or []

                
                for booking in data:
                        if booking["table"] == table:
                            print("Table already booked!")
                            return

                data.append({
                        "name": name,
                        "mobile": mobile,
                        "table": table,
                        "persons": persons
                    })

                self.handler.save_data(self.file, data)

                print("\n✅ Table Booked Successfully")
                self.logger.info(f"Table {table} booked for {name}")


            except Exception as e:
                print("\033[1;31m Something went wrong!\033[0m")  
                self.logger.error(f"Table booking error: {e}")  


    def advance_booking(self):

            try:
                bookings = self.handler.read_data("app/database/tables.json") or []
                self.handler.save_data(self.advance_file, bookings)

                print("\n ====== ADVANCE TABLE BOOKING =====")


                while True:
                    name = input("Enter customer name: ").strip()

                    if not name:
                        print("\033[1;31m Name cannot be empty\033[0m")
                        continue
                    
                    if not name.replace(" ","").isalpha():
                        print("\033[1;31m Name must be contain only aplhabets\033[0m")

                        continue
                    
                    if len(name) < 4:
                        print("\033[1;31m Name must be al least 4 charters long\033[0m")
                        continue

                    break

                while True:

                    phone = input("Enter phone number: ").strip()

                    if not phone.isdigit() or len(phone) != 10:

                        print("\033[1;31m Invalid phone number\033[0m")
                        continue
                    break
                
                while True:
                    date = input("Enter data (YYY-MM-DD): ").strip()

                    try:
                        booking_data = datetime.strptime(date,"%Y-%m-%d")

                        if booking_data.date() < datetime.now().date():
                            print("\033[1;31m Cannot book past date\033[0m")
                            continue
                        break
                    except:

                        print("\033[1;31m Invalid date format\033[0m")
                        continue

                while True:

                    time = input("Enter time (HH:MM): ").strip()

                    try:
                        datetime.strptime(time, "%H:%M")
                        break

                    except:
                        print("\033[1;31mInvalid time format\033[0m")
                        continue

                while True:    

                    table = input("Enter table number: ") .strip()

                    if not table.isdigit():
                        print("\033[1;31m Invalid table number\033[0m") 
                        continue
                    
                    
                    table= int(table)

                    if table < 1 or table > self.total_tables:
                        print(f" Only {self.total_tables} tables available (1- {self.total_tables})")
                        continue

                    break
                    
                for book in bookings:
                    if(
                        book.get("table") == table and
                        book.get("date") == date and
                        book.get("time") == time
                    ):
                        print(" Table already booked at this time")
                        return
                        
                booking = {

                    "name": name,
                    "phone": phone,
                    "date": date,
                    "time": time,
                     "table": table

                } 
                bookings.append (booking)
                self.handler.save_data(self.advance_file, bookings)

                print("✅ Advance table booked successfully")
                self.logger.info(f"Advance booking: Table {table} for {name}")

            except Exception as e:
                print("\033[1;31m Error while advance booking:", e, "\033[0m")
                self.logger.error(f"Advance booking error: {e}")

                    
                        

                        

        
            






