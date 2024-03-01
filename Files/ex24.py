def reverse_lines(read_file, write_file):
    with open(read_file, 'r') as read_text, open (write_file, 'w') as write_text:
        for line in read_text:
            write_text.write(f'{line.rstrip()[::-1]}\n')


reverse_lines('ex24.txt', 'ex24_reversed.txt')