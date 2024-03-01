import re


def sum_integers_in_line(file):
    text = open(file, 'r')
    sum_of_all = 0
    for line in text:
        for element in re.findall(r'\s\d+\s', line):
            sum_of_all += int(element)

    text.close()
    return sum_of_all


print(sum_integers_in_line('sample.txt'))