class MyRange:
    def __init__(self, start, stop=0, step=1):
        if not stop:
            stop = start
            start = 0
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        current = self.current
        self.current += self.step
        return current


mr = MyRange(1,2)
print(list(mr))