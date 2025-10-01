import sys
from bank_account import BankAccount

def main():
    """
    Parses command line arguments to interact with the BankAccount class.
    """

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
        print(f"Deposited: ${amount:.2f}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")

    elif command == "display" and amount is None:
        account.display_balance()

    else:
        print("Invalid command or missing amount.")
        sys.exit(1)


if __name__ == "__main__":
    main()
