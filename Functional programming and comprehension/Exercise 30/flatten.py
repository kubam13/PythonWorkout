def flatten(list_of_lists):
    new_list = [element for single_list in list_of_lists for element in single_list]
    return new_list


print(flatten([[1,2], [3,4]]))