class Firstlast:
    def __init__(self, variable):
        self.variable = variable

    def firstlast(self):
        return self.variable[:1] + self.variable[-1:]

    def even_odd_sums(self):
        sum_even = sum(self.variable[1::2])
        sum_odd = sum(self.variable[::2])

        return [sum_odd, sum_even]

    def plus_minus(self):
        return self.variable[0] + sum(self.variable[1::2]) - sum(self.variable[2::2])

    def myzip(self, *args):
        result = zip(self.variable, *args)
        return list(result)


abc = Firstlast('abcedfghijk')
numb = Firstlast([10,20,30,40,50,60])
zip_var = Firstlast([10,20,30])


print(abc.firstlast())
print(numb.even_odd_sums())
print(numb.plus_minus())
print(zip_var.myzip('abc','dfg'))