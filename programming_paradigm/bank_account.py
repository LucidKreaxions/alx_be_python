class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds are available"""
        if amount > 0 and amount <= self._account_balance:
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
