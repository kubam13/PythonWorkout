def get_item(argument):
    def f(data_structure):
        return data_structure[argument]
    return f


mydict = {'a':1, 'b':2}

function = get_item('a')
result = function(mydict)
print(result)



