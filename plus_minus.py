def plus_minus(numbers):

    return (numbers[0] + sum(numbers[1::2]) - sum(numbers[2::2]))

print(plus_minus([10,20,30,40,50,60]))