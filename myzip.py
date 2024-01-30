def myzip(*args):

    result = zip(*args)
    return list(result)


print(myzip([10,20,30],'abc','dfg'))