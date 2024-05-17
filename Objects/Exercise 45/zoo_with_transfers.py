import all_animals
import cage
from zoo import Zoo


def transfer_animals(self, target_zoo, animal):
    target_zoo.cages_in_zoo[0].add_animals(animal)
    for one_cage in self.cages_in_zoo:
        for one_animal in one_cage.animals_in_cage:
            if one_animal == animal:
                one_cage.animals_in_cage.remove(animal)
                break


Zoo.transfer_animals = transfer_animals


snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')

c1 = cage.Cage(1)
c1.add_animals(wolf, sheep, snake)


c2 = cage.BigCage(2)
c2.add_animals(black_wolf)

c3 = cage.Cage(3)
c3.add_animals(parrot)

c4 = cage.Cage(4)
c4.add_animals(sheep)


z1 = Zoo()
z1.add_cages(c1, c2)

z2 = Zoo()
z2.add_cages(c3, c4)

if __name__ == '__main__':
    z1.transfer_animals(z2, wolf)
    print(z1)
    print(z2)

