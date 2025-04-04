# exAuto.py

import automobile
import  car  # type: ignore
import truck

def main():
    mycar = car.Car('Nissan', 2000, 100000, 7000, 2)

    #Way 2
    print(f'The information of my car: \n{mycar}')
    print()


    #Way 1
    print(f'The information of my car: \n ')
    print(f'\tMake: {mycar.getMake()}\n')
    print(f'\tModel: {mycar.getModel()}\n')
    print(f'\tMileage: {mycar.getMileage()}\n')
    print(f'\tPrice: {mycar.getPrice()}\n')
    print(f'\tDoor Style: {mycar.getDoors()}\n')

    mytruck = truck



if __name__ == '__main__':
    main()
    

