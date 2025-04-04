
#excircle1.py

#import math
import circle
    
def show(ob):
    ob.setRadius(50)
    print(f'Radius: {ob.getRadius()} \t' +\
          f'Area: {ob.getArea():.4f}\t') +\
          f'Circumference: {ob.getCircumference():.4f}\n'


def main():
    c1 = circle.Circle()
    #way 1
    print(f'The area of the circle of radius {c1.getRadius()} is {c1.getArea():.4f}.')
    print()
    #way 3
    show(c1)
    print()
    #way 2 - __str__()
    print(c1)
    print()


    c2 = circle.Circle(5)
    print(f'The area of the circle of radius {c2.getRadius()} is {c2.getArea():.4f}.')
    print()
    print(c2)
    print()
    show(c2)
    print()

if __name__ == '__main__':
    main()


