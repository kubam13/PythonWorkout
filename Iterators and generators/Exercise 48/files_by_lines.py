import os


def all_lines(path):
    for one_file in os.listdir(path):
        full_filename = os.path.join(path, one_file)
        line_list = []

        try:
            for line in open(full_filename):
                line_list.append(line.strip('\n'))
        except OSError:
            pass
        yield line_list


files = list(all_lines('../Files'))
max_length = max(len(lines) for lines in files)

for i in range(max_length):
    for file in files:
        try:
            print(file[i])
        except IndexError:
            pass


#
#
# def all_lines(path):
#     all_lines = []
#     for one_file in os.listdir(path):
#         full_filename = os.path.join(path, one_file)
#         file_lines = []
#
#         try:
#             for line in open(full_filename):
#                 file_lines.append(line.strip('\n'))
#         except OSError:
#             pass
#         all_lines.append(file_lines)
#
#     return all_lines
#
#
# files = all_lines('../Files')
# max_length = max(len(lines) for lines in files)
#
#
# for i in range(max_length):
#     for file in files:
#         try:
#             print(file[i])
#         except IndexError:
#             pass