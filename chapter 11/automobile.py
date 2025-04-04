
# automobile.py

class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def setMake(self, make):
        self.__make = make
    
    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def setPrice(self, price):
        self.__price = price

    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getMileage(self):
        return self.__mileage
    
    def getPrice(self):
        return self.__price
    
    def __str__(self):
        return f'Make: {self.getMake()}\n' +\
            f'Model: {self.getModel()}\n' +\
            f'Mileage: {self.getMileage()}\n' +\
            f'Price: {self.getPrice()}\n'

               