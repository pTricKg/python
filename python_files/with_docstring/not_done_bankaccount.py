class BankAccount:

    """ A Simple Bank Accounting Program """
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.dpst = amount
        self.initial_balance += self.dpst
        print("This is your deposit:",self.dpst)
        print("This is your bal after deposit:",self.initial_balance)
        return self.initial_balance
        
            
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.wthdrw = amount
        print("This is your withdrawal:",self.wthdrw)
                
        if self.initial_balance < self.wthdrw:
            self.initial_balance -= self.wthdrw
            print("This is new bal after withdrawal:",self.initial_balance)
            fee = 5
            self.initial_balance = self.initial_balance - fee
            print("New bal after withdrawal:",self.initial_balance,\
                  "including overdraft fee of",fee)
            return self.initial_balance
            
            
    
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        count_fee = 0
        if self.initial_balance < 0:
            count_fee = count_fee + 1
        fees = count_fee * 5
        print("Total fees:",fees)
        return fees


# To Test:
my_account = BankAccount(10)
print("This is your initial account balance:",my_account.get_balance())
my_account.withdraw(15)
my_account.deposit(5)
print ("This is your final account balance:",my_account.get_balance())

