import os


def all_lines(path):
    for one_file in os.listdir(path):
        full_filename = os.path.join(path, one_file)

        try:
            for line in open(full_filename):
                yield line.strip('\n')
        except OSError:
            pass


for one_line in all_lines('../Files'):
    print(one_line)
