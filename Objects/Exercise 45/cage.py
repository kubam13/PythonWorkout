import all_animals


class Cage:
    max_animals = 3

    def __init__(self, id):
        self.id = id
        self.animals_in_cage = []

    def add_animals(self, *animals):
        for animal in animals:
            if len(self.animals_in_cage) < self.max_animals:
                self.animals_in_cage.append(animal)

    def __repr__(self):
        return f'Cage {self.id}\n' + '\n'.join('\t' + str(animal) for animal in self.animals_in_cage)


class BigCage(Cage):
    max_animals = 5


snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')

c1 = Cage(1)
c1.add_animals(snake, wolf, sheep)
c1.add_animals(parrot)


c2 = BigCage(2)
c2.add_animals(snake, wolf, black_wolf)
c2.add_animals(sheep, parrot, sheep)


if __name__ == '__main__':
    print(c1)
    print(c2)
