def join_numbers(x):
    return ','.join(str(number) for number in range(x))


print(join_numbers(15))