class ATM:
    def __init__(self):
        self.users = {"1234": {"pin": "5678", "balance": 1000}}  # Sample user data
        self.current_user = None

    def authenticate_user(self, card_number, pin):
        if card_number in self.users and self.users[card_number]["pin"] == pin:
            self.current_user = card_number
            print("Authentication successful!\n")
            return True
        else:
            print("Invalid card number or PIN.\n")
            return False

    def check_balance(self):
        if self.current_user:
            print(f"Your balance is: ${self.users[self.current_user]['balance']}\n")
        else:
            print("Please authenticate first.\n")

    def withdraw_money(self, amount):
        if self.current_user:
            if 0 < amount <= self.users[self.current_user]['balance']:
                self.users[self.current_user]['balance'] -= amount
                print(f"Withdrawal successful! New balance: ${self.users[self.current_user]['balance']}\n")
            else:
                print("Insufficient funds or invalid amount.\n")
        else:
            print("Please authenticate first.\n")

    def deposit_money(self, amount):
        if self.current_user:
            if amount > 0:
                self.users[self.current_user]['balance'] += amount
                print(f"Deposit successful! New balance: ${self.users[self.current_user]['balance']}\n")
            else:
                print("Invalid deposit amount.\n")
        else:
            print("Please authenticate first.\n")

    def logout(self):
        self.current_user = None
        print("Logged out successfully.\n")


def main():
    atm = ATM()
    print("Welcome to the ATM!")

    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    
    if not atm.authenticate_user(card_number, pin):
        return

    while True:
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw_money(amount)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit_money(amount)
        elif choice == "4":
            atm.logout()
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
