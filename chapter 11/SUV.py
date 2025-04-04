# SUV.py

import automobile

class SUV(automobile.Automobile):
    def __init__(self, make, model, mileage, price, pass_cap):
        automobile.Automobile.__init__(self, make, model, mileage, price)   
        self.__pass_cap = pass_cap

    def setPass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    def getPass_cap(self):
        return self.__pass_cap
    
    def __str__(self):
        return automobile.Automobile.__str__(self) +\
            f'Passenger Capacity: {self.__pass_cap}\n'
        '''
        return f'Make: {self.getMake()}' +\
            f'Model: {self.getModel()}' +\
            f'Mileage: {self.getMileage()}' +\
            f'Price: {self.getPrice()}' +\
            f'Passenger Capacity: {self.__pass_cap}'
        '''
