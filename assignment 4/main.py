#Grishma Gurung
#(4)  Create a Main.py file containing a main() function to test these three classes.

#import shape class, circle class and rectangle class.
import shape
import circle
import Rectangle

#main function to test the three classes
def main():

    # Testing the Shape class
    Myshape = shape.Shape()  
    print()
    print('1. Shape: ')
    print(Myshape)
    print()

    # Testing the Circle class
    Mycircle = circle.Circle()  
    print('2. Circle: ')
    print(Mycircle)
    print()

    # Testing the Rectangle class
    rectangle = Rectangle.Rectangle()  
    print('3. Rectangle: ')
    print(rectangle)
    print()

#call the main function
if __name__ == '__main__':
    main()

#OUTPUT:
'''

1. Shape: 
Color: green
Filled: True


2. Circle: 
Color: green
Filled: True
Radius: 7
Area: 153.94
Perimeter: 43.98

3. Rectangle: 
Color: green
Filled: True
Length: 15
Width: 13
Area: 195.00
Perimeter: 56.00


'''