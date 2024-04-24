def my_enumerate_generator(letters):
    generator_index = 0
    while generator_index < len(letters):
        for one_letter in letters:
            yield generator_index, one_letter
            generator_index += 1


for index, letter in my_enumerate_generator('abc'):
    print(f'{index}: {letter}')