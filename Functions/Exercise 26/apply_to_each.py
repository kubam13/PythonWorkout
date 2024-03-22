def plus_one(number):
    return number+1


def apply_to_each(function, iterable):
    result_list = []
    for element in iterable:
        result_list.append(function(element))

    return result_list


print(apply_to_each(plus_one,[2,3,5,6]))