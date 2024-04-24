import all_animals
import cage


class Zoo:
    def __init__(self):
        self.cages_in_zoo = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages_in_zoo.append(one_cage)

    def animals_by_color(self, color):
        return [one_animal for one_cage in self.cages_in_zoo
                for one_animal in one_cage.animals_in_cage if one_animal.color == color]

    def animals_by_legs(self, legs):
        return [one_animal for one_cage in self.cages_in_zoo
                for one_animal in one_cage.animals_in_cage if one_animal.legs == legs]

    def number_of_legs(self):
        return sum(one_animal.legs for one_cage in self.cages_in_zoo
                   for one_animal in one_cage.animals_in_cage)

    def __repr__(self):
        return f'Zoo\n' + '\n'.join(str(one_cage) for one_cage in self.cages_in_zoo)


snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')

c1 = cage.Cage(1)
c1.add_animals(snake, wolf, sheep)
c1.add_animals(parrot)


c2 = cage.BigCage(2)
c2.add_animals(snake, wolf, black_wolf)
c2.add_animals(sheep, parrot, sheep)


z = Zoo()
z.add_cages(c1, c2)

if __name__ == '__main__':
    print(z)
    print(z.animals_by_color('black'))
    print(z.animals_by_legs(4))
    print(z.number_of_legs())
