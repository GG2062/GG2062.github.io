
#exCoin.py

import coin 

num_toss = 10

def main():
    myCoin = coin.Coin()

    print('In the beginning, ', end = '')
    print(f'The side is {myCoin.getsideup()}.')
    print(myCoin)
    print()

    print(f'Toss the coin {num_toss} times.')
    countHead = 0

    for i in range(num_toss):
        myCoin.toss()
        #print(myCoin.getsideup())
        if myCoin.getsideup() == 'Head':
            countHead += 1

    percentage = countHead/num_toss
    print(f'There are {countHead} heads.')
    print(f'The percentage of head is {percentage:.1%}.')
    print()

if __name__ == '__main__':
    main()
    