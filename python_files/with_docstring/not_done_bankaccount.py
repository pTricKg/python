class BankAccount:

    """ A Simple Bank Accounting Program """
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.dpst = amount
        print("This is your deposit:",self.dpst)
        return self.dpst
            
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.wthdrw = amount
        print("This is your withdrawal:",self.wthdrw)
        
        if self.initial_balance - self.wthdrw < 0:
            fee = self.initial_balance - 5
            print("This is overdraft fee:", fee)
            return fee
        
        return self.wthdrw
    
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance + self.dpst - self.wthdrw
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        
        return fee


# To Test:
my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(5)
print ("This is your account balance:",my_account.get_balance())

