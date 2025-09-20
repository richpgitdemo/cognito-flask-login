"""
Using the Account class example from the beginning of the Week 4 module,
define a child class that represents a savings account.  Provide a means
for calculating the interest in the savings account and applying the interest
to the balance.  Add a summary method that prints the details of the account on one line.

Write a program that processes a small number of accounts in a loop, applies interest where applicable,
and prints the account summary.

Hint:  You may need to use the isinstance() method to determine which class you are working with.

isinstance(object, classinfo) 
Return True if the object argument is an instance of the classinfo argument, 
or of a (direct, indirect, or virtual) subclass thereof. If object is not an 
object of the given type, the function always returns False.
https://docs.python.org/3/library/functions.html#isinstance

"""



class Account:
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def summary(self):
        return f"Account Number: {self.account_number} Balance: ${self.balance}"
        

class SavingsAccount(Account):
    
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    
    
    def apply_interest(self):
        self.balance += (self.balance * self.interest_rate) / 12
        
    def summary(self):
        return f"{super().summary()} {self.interest_rate}"
    
    
    
accounts = []

accounts.append(Account(1, 400.00))
accounts.append(Account(2, 500.00))
accounts.append(SavingsAccount(3, 350, .029))
accounts.append(SavingsAccount(4, 725, .029))


for account in accounts:
    if isinstance(account, SavingsAccount):
        account.apply_interest()
    print(account.summary())