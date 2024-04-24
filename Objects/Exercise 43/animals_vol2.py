class Animal:

    def __init__(self, number_of_legs, color=None):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs.'


class ZeroLeggedAnimal(Animal):
    def __init__(self):
        super().__init__(0)


class TwoLeggedAnimal(Animal):
    def __init__(self):
        super().__init__(2)


class FourLeggedAnimal(Animal):
    def __init__(self):
        super().__init__(4)


class Snake(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__()
        self.color = color


class Parrot(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__()
        self.color = color


class Wolf(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__()
        self.color = color


class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super.__init__()
        self.color = color


s = Snake('blue')
print(s)