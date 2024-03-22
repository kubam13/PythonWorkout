def function_double(x):
    return x*2


def function_plus_one(x):
    return x+1


def doboth(f1, f2):
    def g(x):
        return f2(f1(x))

    return g


both_functions = doboth(function_double, function_plus_one)
result = both_functions(7)
print(result)