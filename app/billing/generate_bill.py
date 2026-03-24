class GenerateBill:

    def generate_bill(self):

        print(" === BILL===")

        item = input("Enter item name: ")
        price = int(input("Enter price Rs: "))
        qty = int(input("Enter quantity: "))

        total = price * qty

        print("\n---- BILL ----")
        print("Item",item)
        print("Price:",price)
        print("Qty:",qty)
        print("Total:",total)
