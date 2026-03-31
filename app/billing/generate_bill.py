from app.utilities.file_handler import FileHandler


class GenerateBill:

     def __init__(self):
  
            self.handler = FileHandler()
            self.file = "app/database/orders.json"

     def generate_bill(self): 

            orders = self.handler.read_data(self.file)

              
            if not orders:
                 print("No order found")
                 return

            last_order = orders[-1] 

            print(" ========= BILL ========")

            total = 0

            for item in last_order["items"]:

               print(f"{item['name']} ({item['size']}) x{item['qty']} = Rs{item['amount']}")
               total += item["amount"]
            gst = total * 0.05
            grand_total = total + gst
            
            print("\n---------------------------------")

            print(f"Subtotal =    Rs{int(total)}")
            print(f"GST (5%) =    Rs{int(gst)}")
            print("------------------------------------")
            print(f"Grand Total = Rs{int(grand_total)}")
            print("------------------------------------")

            print("\nPayment Method:")
            print("\033[1;37m1. UPI")
            print("2. Cash")
            print("3. Card")

            choice = input("Choose payment: ")


            if choice == "1":
                print("Paid via UPI")
            elif choice == "2":
                 print("Paid via Cash")
            elif choice == "3":
                 print("Paid via Card")
            else:
                 print("Invalid payment")
                 return
            print("Paid via", choice)

            print("\n✅ Payment Successful")

            orders[-1]["status"] = "paid"
            self.handler.save_data(self.file,orders)
               

             
             