def strip_and_upper(text):
    return f'{text.strip().upper()}\n'


def reverse_lines(function, read_file, write_file):
    with open(read_file, 'r') as read_text, open (write_file, 'w') as write_text:
        for line in read_text:
            write_text.write(function(line))


reverse_lines(strip_and_upper, '../../Files/second_sample.txt', 'result.txt')