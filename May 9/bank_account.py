class BankAccount:
    """Class to represent a bank account with deposit, withdraw, and balance check functionality"""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize account with holder name and optional initial balance"""
        self._account_holder = account_holder 
        self._balance = initial_balance       
        
    def deposit(self, amount):
        """Deposit money into the account"""
        try:
            amount = float(amount)
            if amount <= 0:
                print("Error: Deposit amount must be positive")
                return False
            self._balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
            return True
        except ValueError:
            print("Error: Invalid amount entered")
            return False
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        try:
            amount = float(amount)
            if amount <= 0:
                print("Error: Withdrawal amount must be positive")
                return False
            if amount > self._balance:
                print("Error: Insufficient funds")
                return False
            self._balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
            return True
        except ValueError:
            print("Error: Invalid amount entered")
            return False
    
    def get_balance(self):
        """Display and return the current balance"""
        print(f"Account balance for {self._account_holder}: ${self._balance:.2f}")
        return self._balance
    
    def get_account_holder(self):
        """Return the account holder's name"""
        return self._account_holder

def main():
    # Get account holder name and initial balance from user
    holder = input("Enter account holder name: ").strip()
    try:
        initial_balance = float(input("Enter initial balance (default 0): ") or 0)
    except ValueError:
        initial_balance = 0
        print("Invalid input. Initial balance set to $0.00")
    
    # Create bank account
    account = BankAccount(holder, initial_balance)
    
    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            amount = input("Enter amount to deposit: ").strip()
            account.deposit(amount)
        
        elif choice == '2':
            amount = input("Enter amount to withdraw: ").strip()
            account.withdraw(amount)
        
        elif choice == '3':
            account.get_balance()
        
        elif choice == '4':
            print(f"Goodbye, {account.get_account_holder()}!")
            break
        
        else:
            print("Error: Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()