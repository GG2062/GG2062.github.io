
#circle.py

import math

class Circle:
    
    def __init__(self, r = 1):  #initializer
        self.__radius = r       #private

    def setRadius(self, r):
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return math.pi * self.__radius * self.__radius
    
    def getCircumference(self):
        return 2 * math.pi * self.__radius
    
    def __str__(self):
        return f'Radius: {self.__radius}\n' +\
               f'Area: {self.getArea():.4f}\n' +\
               f'Circumference: {self.getCircumference():.4f}\n'
    
    