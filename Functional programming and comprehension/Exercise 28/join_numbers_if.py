def join_numbers_if(x):
    list_of_numbers = [str(number) for number in range(x) if number<=10]
    return ','.join(list_of_numbers)


print(join_numbers_if(12))