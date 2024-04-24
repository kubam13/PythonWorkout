class Beverage:
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature


coke = Beverage('cola', 0)
print(coke.temperature)

beer = Beverage('Kuflowe mocne', 30)
print({beer.name: beer.temperature})

tea = Beverage('Herbata')
print({tea.name: tea.temperature})