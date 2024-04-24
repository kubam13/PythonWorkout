class Animal:

    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs.'


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


s = Sheep('white')
# print(s.species)
# print(s.color)
# print(s.number_of_legs)
# print(s)


w = Wolf('grey')
print(w)

sn = Snake('yellow')
# print(sn.number_of_legs)

p = Parrot('red')
print(p)
