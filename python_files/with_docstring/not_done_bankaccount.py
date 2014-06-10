class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        my_account = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        my_account = my_account + amount
        return my_account
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        my_account = my_account - amount
        return my_account
    def get_balance(self):
        """Returns the current balance in the account."""
        return my_account
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        if my_account < 0:
            fee = my_account - 5
        return fee    
