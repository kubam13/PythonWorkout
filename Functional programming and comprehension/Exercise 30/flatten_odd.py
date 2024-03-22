def flatten_odd_ints(list_of_lists):
    new_list = [element for single_list in list_of_lists for element in single_list if element.is_integer()
                and not element % 2 == 0]
    return new_list


print(flatten_odd_ints([[1,2], [2,4],['5',5.5]]))