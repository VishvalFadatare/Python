# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:57:28 2024

@author: vishv
"""

class Account:
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
        self.balance -= amt
        print("Withdrawal:",amt,"Balance:",self.balance)
        


class SavingsAccount(Account):
    def interest(self):
        interest = self.balance * 0.05
        self.deposit(interest)
        print("New Balance",self.balance)


savings = SavingsAccount("64", "Vishval")
savings.info(64, "Vishval")
savings.deposit(1000)
savings.withdraw(200)
savings.interest()
