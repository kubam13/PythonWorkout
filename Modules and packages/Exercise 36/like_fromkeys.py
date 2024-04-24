def like_fromkeys(keys, function):
    return {element: function(element) for element in keys}


def f(key):
    return key.upper()
