
#coin.py

import random

class Coin:
    def __init__(self):
        self.__sideup = 'Head'
    
    def toss(self):
        if random.randint(0, 1) == 1:
            self.__sideup = 'Head'
        else:
            self.__sideup = 'Tail'

    def getsideup(self):
        return self.__sideup
    
    def __str__(self):
        return f'sideup: {self.__sideup}\n'
               
