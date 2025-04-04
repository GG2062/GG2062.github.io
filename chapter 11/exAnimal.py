# exAnimal.py

import animal

def showInfo(obj):
    if isinstance(obj, animal.Mammal):
        obj.show_species()
        obj.make_sound()
        print()
    else:
        print('That is not a mammal!')

def main():
    myMammal = animal.Mammal('regular animal')
    myDog = animal.Dog()
    myCat = animal.Cat()

    print('Here are the information: ')
    showInfo(myMammal)

    '''
    myMammal.show_species()
    myMammal.make_sound()
    print()
    '''
    showInfo(myDog)
    '''
    myDog.show_species()
    myDog.make_sound()
    print()
    '''
    showInfo(myCat)
    '''
    myCat.show_species()
    myCat.make_sound()
    print()
    '''
    showInfo('Tra')

if __name__ == '__main__':
    main()



