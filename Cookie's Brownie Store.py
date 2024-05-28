## Cookie's Brownie Store
## Amanda M
## 05/28/2024

def brownies():
    quantity_b = input("How many brownies would you like?")
    if quantity_b < 1:
        print("You have to order something!")
        quantity_b
    elif quantity_b > 10:
        print("You'll buy our whole stock! Please go lower.")
    ... # I'll add "continue to Order Number" or "Print Order number" here later

def cookies():
    quantity_c = input("How many cookies would you like?")
    if quantity_c < 1:
        print("You have to order something!")
        quantity_c
    elif quantity_c > 11:
        print("You'll buy our whole stock! Please go lower.")

def pies():
    quantity_d = input("How many cookies would you like?")
    if quantity_d < 1:
        print("You have to order something!")
        quantity_d
    elif quantity_d > 6:
        print("You'll buy our whole stock! Please go lower.")

def ticketsys():                # Majority of this I got off this website (https://codepal.ai/code-generator/query/LK87d6eS/python-ticketing-system) but I just need to breakdown the parts I need for later.
    def orderconfig(self, product, quantity, number):
        self.tickets = []

        ticket = {
            'product' = product,
            'quantity' = quantity,
            'number' = number,
        }
        self.tickets.append(ticket)

    def see_ticket(self):
        if not self.tickets:
            print("No orders available.")
        else:
            for idx, ticket in enumerate(self.tickets, 1):
                print(f"Ticket {idx}")
                print(f"Product: {ticket['product']}")
                print(f"Quantity: {ticket['quantity']}")
                print(f"Number: {ticket['number']}")
                print()

def shop_menu():
    print("Welcome to Cookie's Brownie! What would you like to order?")
    a = input("1. Brownies,   2. Cookies,   3. Pies,    4. Order Number")
    def catchselect(selection:str):
        match selection:
            case "1":
                brownies()
            case "2":
                cookies()
            case "3":
                pies()
            case "4":
                ticketsys()

shop_menu()