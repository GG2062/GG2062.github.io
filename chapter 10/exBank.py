
# exBank.py

import BankAccount 

def main():
    myAccount = BankAccount.BankAccount()

    accnum = input('Enter the account number: ')
    balance = int(input('Enter your starting balance: '))

    myAccount.setAccNum(accnum)
    myAccount.setBalance(balance)

    print(f'Your account number is {myAccount.getAccount()}')
    print(f'Your balance is {myAccount.getBalance()}.')
    print()
    print(accnum )
    print(balance)

if __name__ == '__main__':
    main()




