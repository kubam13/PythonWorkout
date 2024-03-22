family = {'Maro': [{'name':'Leokadia','age':12}, {'name':'Cyceron','age':1}, {'name':'Denis','age':9}],
          'Eustachy': [{'name':'Frank','age':52}, {'name':'GG','age':3}]}


def grandchildren(family_dict):
    grandchildren = sorted([child for children in family_dict.values() for child in children],
                           key=lambda x: x['age'], reverse=True)
    grandchildren_names_sorted = [child['name'] for child in grandchildren]
    return grandchildren_names_sorted


print(grandchildren(family))