import operator


def calc(math_expression):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '%': operator.mod,
                  '**': operator.pow}
    operation = math_expression.split()[0]
    a = int(math_expression.split()[1])
    b = int(math_expression.split()[2])
    result = operations[operation](a, b)
    return result


print(calc('/ 12 5'))
