# main-0.py (CORRECTED VERSION)
import sys
from bank_account import BankAccount 

def main():
    account = BankAccount(100.00)  

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_arg = sys.argv[1].split(':')
        command = command_arg[0].lower()
        amount = float(command_arg[1]) if len(command_arg) > 1 else None
    except (ValueError, IndexError):
        command = sys.argv[1].lower() if len(sys.argv) > 1 else ""
        amount = None
    
    
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        # FIX: Ensure output includes .2f formatting
        print(f"Deposited: ${amount:.2f}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            # FIX: Ensure output includes .2f formatting
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    elif command == "display" and amount is None:
        # NOTE: display_balance in bank_account.py already handles .2f
        account.display_balance() 

    else:
        print("Invalid command or missing amount.")
        sys.exit(1)

if __name__ == "__main__":
    main()
