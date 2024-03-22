import operator
from functools import reduce


def calc(math_expression):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '%': operator.mod,
                  '**': operator.pow}
    operation = math_expression.split()[0]
    numbers = math_expression.split()[1:]
    numbers = [int(number) for number in numbers]
    result = reduce(operations[operation], numbers)
    print(result)


calc('** 2 1 3 2')