class Animal:

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs.'


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0


class TwoLeggedAnimal(Animal):
    number_of_legs = 2


class FourLeggedAnimal(Animal):
    number_of_legs = 4


class Snake(ZeroLeggedAnimal):

    def __init__(self, color):
        super().__init__(color, self.number_of_legs)


class Parrot(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__(color, self.number_of_legs)


class Wolf(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color, self.number_of_legs)


class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color, self.number_of_legs)


s = Sheep('gay')
print(s)