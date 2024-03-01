def get_final_line(file):
    text = open(file, 'r')
    return text.readlines()[-1]


print(get_final_line('apache.txt'))
