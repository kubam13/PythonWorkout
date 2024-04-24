import all_animals


class Cage:
    compatibility_dict = {'Sheep': ['Snake', 'Parrot'],
                          'Snake': ['Sheep', 'Wolf'],
                          'Wolf': ['Snake', 'Parrot'],
                          'Parrot': ['Sheep', 'Wolf']}

    def __init__(self, id):
        self.id = id
        self.animals_in_cage = []

    def add_animals(self, *animals):
        for animal in animals:
            for animal_in_cage in self.animals_in_cage:
                if type(animal).__name__ not in self.compatibility_dict[type(animal_in_cage).__name__]:
                    raise Exception('Sorry those 2 animals cant be together')
            self.animals_in_cage.append(animal)

    def __repr__(self):
        return f'Cage {self.id}\n' + '\n'.join('\t' + str(animal) for animal in self.animals_in_cage)


snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')

c1 = Cage(1)
c1.add_animals(sheep, snake)
print(c1)

c1.add_animals(parrot)
