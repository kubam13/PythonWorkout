class RecentDict(dict):
    def __init__(self, number):
        self.number = number

    def __setitem__(self, key, value):
        if len(self) >= self.number:
            oldest = next(iter(self))
            del self[oldest]
        super().__setitem__(key, value)


r1 = RecentDict(5)
r1[1] = 'a'
r1[2] = 'b'
r1[3] = 'c'
r1[4] = 'd'
r1[5] = 'e'
print(r1)

r1[6] = 'f'

print(r1)

