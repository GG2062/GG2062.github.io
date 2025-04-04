
# BankAccount.py

class BankAccount:
    
    def __init__(self, accNum = '', bal = 0):
        self.__AccNum = accNum
        self.__balance = bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Invalid! No enough money!')

    def getAccount(self):
        return self.__AccNum
    
    def getBalance(self):
        return self.__balance
    
    def setAccNum(self, accNum):
        self.__AccNum = accNum

    def setBalance(self, bal):
        self.__balance = bal

    def __str__(self):
        return f'Account Number: {self.__AccNum}\n' +\
               f'Account Balance: {self.__balance}'
