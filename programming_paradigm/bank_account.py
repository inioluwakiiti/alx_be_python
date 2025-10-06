class BankAccount:
    """
    A simple Bank Account class to demonstrate OOP concepts.
    """
    def __init__(self, initial_balance=0.0):
        """
        Initializes the bank account with a starting balance.
        """
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """
        Must accept 'amount' and return bool
        """
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
