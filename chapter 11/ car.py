# car.py

import automobile

class Car(automobile.Automobile):
    def __init__(self, make, model, mileage, price, doors):
        automobile.Automobile.__init__(self, make, model, mileage, price)   
        self.__doors = doors

    def setDoors(self, doors):
        self.__doors = doors

    def getDoors(self):
        return self.__doors
    
    def __str__(self):
        return super().__str__() +\
            f'Door Style: {self.__doors}\n'
    
        '''
        return automobile.Automobile.__str__(self) +\
            f'Door Style: {self.__doors}\n'
        '''

        '''
        return f'Make: {self.getMake()}\n' +\
            f'Model: {self.getModel()}\n' +\
            f'Mileage: {self.getMileage()}\n' +\
            f'Price: {self.getPrice()}\n' +\
            f'Door Style: {self.__doors}\n'
        '''
