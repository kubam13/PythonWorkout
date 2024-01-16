class Exercise11:
    def __init__(self, variable):
        self.variable = variable

    def alphabetize_names(self):
        return sorted(self.variable, key=lambda i: (i['last'], i['first']))

    def sort_absolutes(self):
        return sorted(self.variable, key=lambda i: abs(i))

    def sort_vowels(self):
        return sorted(self.variable, key=lambda string: sum(i in 'aeiou' for i in string))

    def sort_numbers(self):
        return sorted(self.variable, key=lambda number: sum(number))


people = Exercise11([{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'}, {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'}, {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'}])
numbers = Exercise11((-1,2, -6, 4, -15, 11))
list_of_strings= Exercise11(["ab", "kuba", "cooo", "xx","wwa"])
list_of_numbers= Exercise11([[1,2,3], [], [4], [12,4,1], [5,6,9]])

print(people.alphabetize_names())
print(numbers.sort_absolutes())
print(list_of_strings.sort_vowels())
print(list_of_numbers.sort_numbers())



