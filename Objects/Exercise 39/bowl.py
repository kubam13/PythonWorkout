class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for element in new_scoops:
            self.scoops.append(element)

    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('carmel')

b = Bowl()
b.add_scoops(s1, s2)
print(b)