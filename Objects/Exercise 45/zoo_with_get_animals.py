import all_animals
import cage
from zoo import Zoo


def get_animals(self, **kwargs):
    valid_keys = ['color', 'legs']

    return [one_animal for one_cage in self.cages_in_zoo for one_animal in one_cage.animals_in_cage
            if all(getattr(one_animal, name) == value for name, value in kwargs.items()
                   if name in valid_keys)]


Zoo.get_animals = get_animals

snake = all_animals.Snake('yellow')
wolf = all_animals.Wolf('white')
parrot = all_animals.Parrot('red')
sheep = all_animals.Sheep('black')
black_wolf = all_animals.Wolf('black')
yelawolf = all_animals.Wolf('yellow')

c1 = cage.Cage(1)
c1.add_animals(black_wolf, sheep, snake)

c2 = cage.BigCage(2)
c2.add_animals(snake, yelawolf)

z1 = Zoo()
z1.add_cages(c1, c2)

if __name__ == '__main__':
    print(z1.get_animals(color='black'))
    print(z1.get_animals(legs=0))
    print(z1.get_animals(color='yellow', legs=4))
