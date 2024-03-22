family = {'Maro': ['Leokadia', 'Cyceron', 'Denis'], 'Eustachy': ['Frank', 'GG']}


def grandchildren(family_dict):
    return [child for children in family_dict.values() for child in children]


print(grandchildren(family))