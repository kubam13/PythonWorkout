def circle_generator(letters, max_times):
    for generator_index in range(max_times):
        yield letters[generator_index % len(letters)]


print(list(circle_generator('abcde', 7)))