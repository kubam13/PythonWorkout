def transform_values(function, dictionary):
    return {key: function(value) for (key,value) in dictionary.items()}


d = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x: x+1, d))