def generator_zip(*args):
    zip_range = min(len(arg) for arg in args)
    for i in range(zip_range):
        item_list = []
        for arg in args:
            item_list.append(arg[i])
        yield tuple(item_list)


for item in generator_zip('abc', [10, 20, 30]):
    print(item)

