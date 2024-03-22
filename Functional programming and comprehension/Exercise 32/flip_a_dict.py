
def flip_a_dict(dict_to_flip):
    flipped_dict = {value: key for (key, value) in dict_to_flip.items()}
    return flipped_dict


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(flip_a_dict(my_dict))