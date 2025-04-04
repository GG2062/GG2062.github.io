#Grishma Gurung
#(2)  Create a Circle.py file containing the definition of a class named Circle, which is extended from the Shape class 
# and has one additional private data attribute, radius, an __init__ method and the following methods:
#•	set_radius() - 	assigns a value to the radius field.
#•	get_radius() - 	returns the value of the radius field.
#•	get_area() - 	returns the area of the circle object.
#•	get_perimeter() - returns the perimeter of the circle object.
#•	__str__() - returns a string indicating the state of the circle object.

#import shape class
import shape
#import math for pi
import math

#circle class
class Circle(shape.Shape):

    # initializing color, filled and radius with default values.
    def __init__(self, color = 'green', filled = True, radius = 7):
        #initializing color and filled from the shape class.
        shape.Shape.__init__(self, color = 'green', filled = 'True')   
        #store radius.
        self.__radius = radius

    #set the radius.
    def set_radius(self, radius):
        self.__radius = radius

    #get the radius.
    def get_radius(self):
        return self.__radius
    
    #get the area.
    def get_area(self):
        return math.pi * (self.__radius) ** 2
    
    #get the perimeter.
    def get_perimeter(self):
        return 2 * math.pi * self.__radius
    
    #returns color, filled, radius, area and perimeter of the circle as a string.
    def __str__(self):
        return f'Color: {self.get_color()}\n' +\
               f'Filled: {self.is_filled()}\n' +\
               f'Radius: {self.get_radius()}\n' +\
               f'Area: {self.get_area():.2f}\n' +\
               f'Perimeter: {self.get_perimeter():.2f}'