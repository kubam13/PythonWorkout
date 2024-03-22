def transform_values(function, function_check, dictionary):
    return {key: function(value) for (key,value) in dictionary.items() if function_check(key, value)}


def if_key_value(key, value):
    return value > 0


d = {'a':1, 'b':0, 'c':3}
print(transform_values(lambda x: x+1, if_key_value, d))