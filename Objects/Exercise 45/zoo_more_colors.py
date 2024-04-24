import all_animals
import cage

from zoo import Zoo


def new_animals_by_color(self, *colors):
    animals_by_color_list = []
    if not colors:
        raise Exception('You have not passed any colors')
    for color in colors:
        animals_by_color_list.extend([one_animal for one_cage in self.cages_in_zoo
                                     for one_animal in one_cage.animals_in_cage
                                     if one_animal.color == color])
    return animals_by_color_list


Zoo.animals_by_color = new_animals_by_color

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
    print(z.animals_by_color('black'))
    print(z.animals_by_color('black', 'yellow'))
    print(z.animals_by_color())
