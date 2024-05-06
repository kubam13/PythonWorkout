import os


def all_lines(path, string):
    for one_file in os.listdir(path):
        full_filename = os.path.join(path, one_file)

        try:
            for line in open(full_filename):
                if string in line:
                    yield line.strip('\n')
        except OSError:
            pass


for one_line in all_lines('../Files', 'It'):
    print(one_line)