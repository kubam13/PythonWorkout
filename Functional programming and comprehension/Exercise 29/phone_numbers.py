def phone_numbers(list_of_numbers):
    new_numbers = [next('-'.join([str(int(number.split('-')[0])+1), number.split('-')[1], number.split('-')[2]])
                   for number in list_of_numbers)
                   if not int(number.split('-')[1][0]) > 5 else number for number in list_of_numbers]
    return new_numbers


print(phone_numbers(['123-456-7890', '123-333-4444', '123-777-8888']))
