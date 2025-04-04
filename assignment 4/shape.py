#Grishma Gurung
#(1) Create a Shape.py file containing the definition of a class named Shape, which has two private data attributes:
#•	color:  str type with the “green” default value
#•	filled:  bool type with the “True” default value
#The Shape class should have an __init__ method that creates these attributes, and also have the following methods:
#•	set_color() - 	assigns a value to the color field.
#•	get_color() - 	returns the value of the color field.
#•	set_filled() -  	assigns True or False to the filled field.  
#•	is_filled() - 	returns True or False of the filled field.
#•	__str__() - 	returns a string indicating the state of the object.

#shape class
class Shape:
    
    # initializing color and filled with default values.
    def __init__(self, color = 'green', filled = 'True'):
        #store color and filled.
        self.__color = color
        self.__filled = filled

    #set the color.
    def set_color(self, color):
        self.__color = color

    #get the color.
    def get_color(self):
        return self.__color
    
    #set the filled.
    def set_filled(self, filled):
        self.__filled = filled
    
    #check if the shape is filled.
    def is_filled(self):
        return self.__filled

    #returns color and filled of the shape as a string.
    def __str__(self):
        return f'Color: {self.get_color()}\n' +\
               f'Filled: {self.is_filled()}\n'

