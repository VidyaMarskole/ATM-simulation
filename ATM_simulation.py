# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:15:27 2024

@author: lenovo
"""
def check_bal(amount,avl_balance):
    if((avl_balance-amount)<0):
        print("Insufficient Balance")
        return False
    else:
        return True
    
class ATM:
    def __init__(self, balance=0):
        self.balance=balance
    def check_balance(self):
        print("Available balance:",self.balance)
        print()
    def Deposit(self,amount):
        self.balance+=amount
        self.check_balance()
    def withdraw(self,amount):
        if(check_bal(amount, self.balance)):
            self.balance-=amount
        self.check_balance()


def atm_simulation():
    atm=ATM(1000.00)   #initial balance 
    print('Welcome to ATM simulation')
    while(True):
         print('ATM operation')
         print('1. Check Balance')
         print('2. Deposit')
         print('3. Withdraw ')
         print('4. Exit')
         choice=int(input('Enter the number corresponding to your choice: '))
         if(choice==1):
             atm.check_balance()
         if(choice==2):
             amount=float(input('Enter the deposit amount:'))
             atm.Deposit(amount)
         if(choice==3):
             amount=float(input('Enter the withdraw amount: '))
             atm.withdraw(amount)
         if(choice==4):
             print('Thank you\nFor using ATM simulation \n ')
             break


atm_simulation()
