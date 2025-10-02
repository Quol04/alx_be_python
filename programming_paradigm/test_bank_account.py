#!/usr/bin/env python3

from bank_account import BankAccount

def test_bank_account():
    """Test the BankAccount class functionality."""
    
    print("=== Testing BankAccount Class ===\n")
    
    # Create a new account with initial balance
    print("1. Creating account with $100 initial balance:")
    account = BankAccount(100)
    account.display_balance()
    
    print("\n2. Depositing $50:")
    account.deposit(50)
    
    print("\n3. Withdrawing $30:")
    account.withdraw(30)
    
    print("\n4. Attempting to withdraw $200 (should fail):")
    account.withdraw(200)
    
    print("\n5. Final balance:")
    account.display_balance()
    
    print(f"\n6. Getting balance programmatically: ${account.get_balance():.2f}")
    
    print("\n=== Testing Edge Cases ===\n")
    
    print("7. Testing invalid deposit (negative amount):")
    account.deposit(-10)
    
    print("\n8. Testing invalid withdrawal (negative amount):")
    account.withdraw(-5)
    
    print("\n9. Testing zero deposit:")
    account.deposit(0)

if __name__ == "__main__":
    test_bank_account()