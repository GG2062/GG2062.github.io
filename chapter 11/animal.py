
# animal.py

class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print(f'I am a {self.__species}.')

    def make_sound(self):
        print('Grrrrr')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Dog')
        #super().__init__('Dog')

    def make_sound(self):
        print('Woof! Woof!')

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Cat')
        #super().__init__('Cat')

    def make_sound(self):
        print('Meow')



        
    