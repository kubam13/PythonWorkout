def family_names_letters(family):
    return {letter for name in family for letter in name.lower()}


family_names = ['Michal', 'Kasia', 'Kamil', 'Kuba']
print(family_names_letters(family_names))