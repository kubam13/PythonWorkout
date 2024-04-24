class MyEnumerate:
    def __init__(self, data, starting_index=0):
        self.data = data
        self.index = 0
        self.starting_index = starting_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.starting_index, self.data[self.index])
        self.starting_index += 1
        self.index += 1
        return value


e = MyEnumerate('abc')
for index, letter in e:
    print(f'{index}: {letter}')