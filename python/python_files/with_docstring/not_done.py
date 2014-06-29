class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        initial_blance = None
    def deposit(self, amount):
        """Deposits the amount into the account."""
        initial_balance = initial_balance + amount
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        initial_balance = initial_balance - amount
    def get_balance(self):
        """Returns the current balance in the account."""
        return initial_balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        if initial_balance < 0:
            fee = initial_balance - 5
        return fee    
