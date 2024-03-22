from collections import Counter


def popular_hobbies(names_hobbies_list):
    list_of_hobbies = [element for single_list in [single_dict['hobbies'] for single_dict in names_hobbies_list]
                       for element in single_list]
    most_common_hobbies = Counter(list_of_hobbies).most_common(3)
    return [hobby[0] for hobby in most_common_hobbies]


my_list_of_dicts = [{'name': 'Maro', 'hobbies': {'billiard','football', 'climbing','reading'}},
                    {'name': 'Bob', 'hobbies': {'football', 'reading'}},
                    {'name': 'Claire', 'hobbies': {'reading', 'climbing'}},
                    {'name': 'Brian', 'hobbies': {'killing'}}]

print(popular_hobbies(my_list_of_dicts))