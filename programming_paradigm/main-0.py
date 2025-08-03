# main-0.py for Command Line Interaction:
# This script utilizes BankAccount through command line arguments for banking operations.

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
# Sample Command Line Usage and Expected Outputs:
# Deposit:
#    python main-0.py deposit:50
# Expected Output: Deposited: $50

# Withdraw with Sufficient Funds:
#    python main-0.py withdraw:20
# Expected Output: Withdrew: $20

# Withdraw with Insufficient Funds:
#    python main-0.py withdraw:150
# Expected Output: Insufficient funds.

# Display Balance:
#    python main-0.py display
# Expected Output: Current Balance: $[amount]