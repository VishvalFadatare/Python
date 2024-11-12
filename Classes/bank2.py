# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:04:32 2024

@author: vishv
"""

class Bank:
    def __init__(self, bname):
        self.bname = bname

    def display(self):
        print("Welcome to ",self.bname)
        
class Account(Bank):
    def __init__(self, accnum, name):
        self.accnum = accnum
        self.name = name
        self.balance = 0
        
    def info(self,name,accnum):
        print("Name:",self.name)
        print("account number:",self.accnum)

    def deposit(self, amt):
        self.balance += amt
        print("Deposite:",amt,"Balance:",self.balance)

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Withdrawal:",amt,"Balance:",self.balance)
        else:
            print("Insufficient funds.")


class SavingsAccount(Account):
    def interest(self):
        interest = self.balance * 0.05  # Fixed interest rate of 5%
        self.deposit(interest)
        print("New Balance",self.balance)
        
b=Bank("ABC")
b.display()
        
savings = SavingsAccount("64", "Vishval")
savings.info(64, "Vishval")
savings.deposit(1000)
savings.withdraw(200)
savings.interest()        
    