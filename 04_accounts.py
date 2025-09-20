"""
Using the Account class example from the beginning of the Week 4 module, define a child class that represents a savings account.  Provide a means for calculating the interest in the savings account and applying the interest to the balance.  Add a summary method that prints the details of the account on one line.

Write a program that processes a small number of accounts in a loop, applies interest where applicable, and prints the account summary.

Hint:  You may need to use the isinstance() method to determine which class you are working with.
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
        return f"Account Number: {self.account_number} Balance: ${round(self.balance, 2)}"