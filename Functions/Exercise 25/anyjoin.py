def anyjoin(elements, glue=' '):
    result = glue.join([f'{element}' for element in elements])
    return result


print(anyjoin([1,2,3],'**'))