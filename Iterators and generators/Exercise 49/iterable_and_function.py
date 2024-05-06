def function_on_iterable(iterable, function):
    for element in iterable:
        if function(element):
            yield element


def check_if_b(argument):
    if argument == 'b':
        return True


for i in function_on_iterable('abcd', check_if_b):
    print(i)


for i in function_on_iterable('abCd', lambda x: x.islower()):
    print(i)