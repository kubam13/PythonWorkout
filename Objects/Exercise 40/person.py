class Person:
    population = 0

    def __init__(self):
        Person.population += 1

    def __del__(self):
        Person.population -= 1


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()

print(Person.population)
print(p1.population)

del p2
print(Person.population)
print(p1.population)
