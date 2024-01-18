def myzip(numbers, letters):

    result = zip(numbers,letters)
    return list(result)

print(myzip([10,20,30],'abc'))