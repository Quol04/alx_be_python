
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        
        self.account_balance += amount
        # print(f"Deposited ${amount:.2f}. New balance: ${self.account_balance:.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
            
        if amount > self.account_balance:
            return False
        
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.account_balance:.2f}")
    
    # def get_balance(self):
    #     """Get the current account balance."""
    #     return self.account_balance