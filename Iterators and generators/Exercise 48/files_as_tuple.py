import os


def all_lines(path):
    file_count = 0
    for one_file in os.listdir(path):
        file_count += 1
        line_count = 0
        full_filename = os.path.join(path, one_file)

        try:
            for line in open(full_filename):
                line_count += 1
                yield (one_file, file_count, line_count, line.strip('\n'))
        except OSError:
            pass


for one_line in all_lines('../Files'):
    print(one_line)