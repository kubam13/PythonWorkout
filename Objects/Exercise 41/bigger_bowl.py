class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for element in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(element)

    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('carmel')
s4 = Scoop('water')

bb = BigBowl()
bb.add_scoops(s1, s2, s3, s4, s1, s2)
print(bb)