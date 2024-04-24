class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return MyEnumerateIterator(self.data)

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value


class MyEnumerateIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value


e = MyEnumerate('abc')
print('** A **')
for index, one_item in e:
    print(f'{index}: {one_item}')
print('** B **')
for index, one_item in e:
    print(f'{index}: {one_item}')
print('** C **')
for index, one_item in e:
    print(f'{index}: {one_item}')

