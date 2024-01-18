def even_odd_sums(numbers):

    sum_even = sum(numbers[1::2])
    sum_odd = sum(numbers[::2])

    return [sum_odd, sum_even]

    

print(even_odd_sums([10,20,30,40,50,60]))