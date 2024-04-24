class Animal:

    def __init__(self, color, legs, sound, space_required):
        self.species = self.__class__.__name__
        self.color = color
        self.legs = legs
        self.sound = sound
        self.space_required = space_required

    def __repr__(self):
        return f'{self.sound.capitalize()} - {self.color} {self.species}, {self.legs} legs.'


class ZeroLeggedAnimal(Animal):
    legs = 0


class TwoLeggedAnimal(Animal):
    legs = 2


class FourLeggedAnimal(Animal):
    legs = 4


class Snake(ZeroLeggedAnimal):
    sound = 'ssss'
    space_required = 1

    def __init__(self, color):
        super().__init__(color, self.legs, self.sound, self.space_required)


class Parrot(TwoLeggedAnimal):
    sound = 'normal human voice'
    space_required = 1

    def __init__(self, color):
        super().__init__(color, self.legs, self.sound, self.space_required)


class Wolf(FourLeggedAnimal):
    sound = 'woof'
    space_required = 5

    def __init__(self, color):
        super().__init__(color, self.legs, self.sound, self.space_required)


class Sheep(FourLeggedAnimal):
    sound = 'baa'
    space_required = 3

    def __init__(self, color):
        super().__init__(color, self.legs, self.sound, self.space_required)


if __name__ =='__main__':
    s = Snake('gay')
    print(s.species)

    p = Parrot('also gay')
    print(p)