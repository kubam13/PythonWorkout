class Animal:

    def __init__(self, color, number_of_legs, sound):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
        self.sound = sound

    def __repr__(self):
        return f'{self.sound.capitalize()} - {self.color} {self.species}, {self.number_of_legs} legs.'


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0


class TwoLeggedAnimal(Animal):
    number_of_legs = 2


class FourLeggedAnimal(Animal):
    number_of_legs = 4


class Snake(ZeroLeggedAnimal):
    sound = 'ssss'

    def __init__(self, color):
        super().__init__(color, self.number_of_legs, self.sound)


class Parrot(TwoLeggedAnimal):
    sound = 'normal human voice'

    def __init__(self, color):
        super().__init__(color, self.number_of_legs, self.sound)


class Wolf(FourLeggedAnimal):
    sound = 'woof'

    def __init__(self, color):
        super().__init__(color, self.number_of_legs, self.sound)


class Sheep(FourLeggedAnimal):
    sound = 'baa'

    def __init__(self, color):
        super().__init__(color, self.number_of_legs, self.sound)


s = Snake('gay')
print(s)

p = Parrot('also gay')
print(p)