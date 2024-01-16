def mysum(*variables):

    if not variables:
        variables = 0
        return variables

    output = variables[0]
    for variable in variables[1:]:
        output += variable
    return output


print(mysum(1,2,3))