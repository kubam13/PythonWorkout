import all_animals


class Cage:
    max_space = 15

    def __init__(self, id):
        self.id = id
        self.animals_in_cage = []

    def add_animals(self, *animals):
        for animal in animals:
            if (sum(animal_in_cage.space_required for animal_in_cage in self.animals_in_cage)
                    + animal.space_required > self.max_space):
                raise Exception('Sorry, not enough space for that animal')
            self.animals_in_cage.append(animal)

    def __repr__(self):
        return f'Cage {self.id}\n' + '\n'.join('\t' + str(animal) for animal in self.animals_in_cage)


class BigCage(Cage):
    max_space = 25


snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')

# c1 = Cage(1)
# c1.add_animals(wolf, black_wolf, sheep)
# print(c1)
# c1.add_animals(sheep)
# print(c1)

c2 = BigCage(2)
c2.add_animals(wolf, wolf, black_wolf, sheep)
c2.add_animals(black_wolf, black_wolf)