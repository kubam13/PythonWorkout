from collections.abc import Iterable


class Flatlist(list):
    def append(self, __object):
        if isinstance(__object, Iterable):
            for element in __object:
                self.append(element)
        else:
            super().append(__object)


f1 = Flatlist()
f1.append([10, 20, 30])
print(f1)
f1.append(40)
print(f1)
