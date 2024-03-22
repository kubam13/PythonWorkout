def add_numbers():
    string_of_numbers = input('Enter integers in string: ')
    return sum(int(element) for element in string_of_numbers.split() if element.isdigit())


print(add_numbers())