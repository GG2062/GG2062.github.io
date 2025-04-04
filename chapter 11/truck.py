#truck.py

import automobile

class Truck(automobile.Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        automobile.Automobile.__init__(self, make, model, mileage, price)   
        self.__drive_type = drive_type

    def setDrive_type(self, drive_type):
        self.__drive_type = drive_type

    def getDrive_type(self):
        return self.__drive_type
    
    def __str__(self):
        return automobile.Automobile.__str__(self) +\
            f'Drive Type: {self.__drive_type}\n'
        '''
        return f'Make: {self.getMake()}' +\
            f'Model: {self.getModel()}' +\
            f'Mileage: {self.getMileage()}' +\
            f'Price: {self.getPrice()}' +\
            f'Drive Type: {self.__drive_type}'
        '''
