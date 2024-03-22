def dict_to_tuples(list_of_dicts):
    list_of_tuples = [(key, value) for single_dict in list_of_dicts for key, value in single_dict.items()]
    return list_of_tuples


my_list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25},
                    {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
print(dict_to_tuples(my_list_of_dicts))