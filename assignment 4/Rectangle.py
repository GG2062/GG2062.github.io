#Grishma Gurung
# (3)  Create a Rectangle.py file containing the definition of a class named Rectangle, which is extended from the Shape class 
# and has two additional private data attributes, length and width, an __init__ method and the following methods:
#•	set_length() - 	assigns a value to the length field.
#•	get_length() - 	returns the value of the length field.
#•	set_width() - 	assigns a value to the width field.
#•	get_width() - 	returns the value of the width field.
#•	get_area() - 	returns the area of the rectangle object.
#•	get_perimeter() - returns the perimeter of the rectangle object.
#•	__str__() - returns a string indicating the state of the rectangle object.

#import shape class
import shape

#rectangle class
class Rectangle(shape.Shape):

    # initializing color, filled, length and width with default values.
    def __init__(self, color = 'green', filled = True, length = 15, width = 13):
        #initializing color and filled from the shape class.
        shape.Shape.__init__(self, color = 'green', filled = 'True')  
        #store length and width. 
        self.__length = length
        self.__width = width

    #set the length.
    def set_length(self, length):
        self.__length = length

    #get the length.
    def get_length(self):
        return self.__length
    
    #set the width.
    def set_width(self, width):
        self.__width = width

    #get the width.
    def get_width(self):
        return self.__width

    #get the area.
    def get_area(self):
        return self.__length * self.__width
    
    #get the perimeter.
    def get_perimeter(self):
        return 2 * (self.__length + self.__width)
    
    #returns color, filled, length, width, area and perimeter of the rectangle as a string.
    def __str__(self):
        return super().__str__() +\
            f'Length: {self.get_length()}\n' +\
            f'Width: {self.get_width()}\n' +\
            f'Area: {self.get_area():.2f}\n' +\
            f'Perimeter: {self.get_perimeter():.2f}'