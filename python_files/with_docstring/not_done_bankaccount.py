class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.amount = self.initial_balance + amount
        return amount
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.amount = self.initial_balance - amount
        return self.amount
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        if self.initial_balance < 0:
            fee = self.initial_balance - 5
        return fee


# To Test:
my_account = BankAccount(10)
#my_account.withdraw(15)
my_account.deposit(20)
print (my_account.get_balance())
