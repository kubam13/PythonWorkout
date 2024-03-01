def factors():
    numbers = input('Enter integers separated by spaces: ')
    list_of_numbers = numbers.split(' ')
    factors_dict = {}
    for number in list_of_numbers:
        for i in range(1, int(number) + 1):
            if int(number) % i == 0:
                if i not in factors_dict.keys():
                    factors_dict[i] = [number]
                else:
                    factors_dict[i].append(number)
    return dict(sorted(factors_dict.items()))


print(factors())