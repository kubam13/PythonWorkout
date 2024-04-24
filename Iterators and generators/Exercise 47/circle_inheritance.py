class CircleIterator:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        value = getattr(self, self.returns)[self.index % len(self.data)]
        self.index += 1
        return value

    def __iter__(self):
        return type(self)(self.data, self.max_times)


class Circle(CircleIterator):

    def __init__(self, data, max_times):
        super().__init__(data, max_times)
        self.returns = 'data'


c = Circle('abc', 5)
print(list(c))

e = Circle('def', 4)
print('** A **')
print(list(e))
print('** B **')
print(list(e))