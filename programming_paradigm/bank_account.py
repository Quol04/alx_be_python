
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        
        self.account_balance += amount
        print(f"Deposited: ${amount}")
        return self.account_balance

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
            
        if amount > self.account_balance:
            return False
        
        self.account_balance -= amount
        print(f"Withdrew: ${amount}")
        return self.account_balance

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
    