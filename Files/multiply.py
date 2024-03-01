def multiply_columns(file):
    text = open(file, 'r')
    sum_of_all = 0
    for line in text:
        try:
            result = int(line.strip().split('  ')[0])*int(line.strip().split('  ')[1])
            sum_of_all += result
        except ValueError:
            pass
    return sum_of_all


print(multiply_columns('numbers.txt'))