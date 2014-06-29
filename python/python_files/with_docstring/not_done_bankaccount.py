class BankAccount:

    """ A Simple Bank Accounting Program """
    
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance = initial_balance
        self.count_fees = 0
        
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
            self.count_fees += 5
            self.initial_balance -= self.wthdrw
            print("This is new bal after withdrawal:",self.initial_balance)
            fee = 5
            self.initial_balance = self.initial_balance - fee
            print("New bal after withdrawal:",self.initial_balance,\
                  "including overdraft fee of",fee)
            
            print("Total fee:",fee)
            return self.initial_balance
        else:
            self.initial_balance -= self.wthdrw
            return self.initial_balance
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
    
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.count_fees


# To Test:
##my_account = BankAccount(10)
##print("This is your initial account balance:",my_account.get_balance())
##my_account.withdraw(15)
##my_account.deposit(5)
##print ("This is your final account balance:",my_account.get_balance())
##print ("Your total fee:",my_account.get_fees())
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5) 
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50) 
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25) 
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5) 
print (my_account.get_balance(), my_account.get_fees())
