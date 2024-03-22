def factorial(*args):
    factorial = 1
    for arg in args:
        factorial *= arg

    return factorial


print(factorial(1,3,5,6))