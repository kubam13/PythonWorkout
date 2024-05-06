import os


def file_usage_timing(directory):
    for file in os.listdir(directory):
        file_fullname = os.path.join(directory, file)
        yield (file, os.stat(file_fullname).st_atime, os.stat(file_fullname).st_mtime,
               os.stat(file_fullname).st_ctime)


for file_info in file_usage_timing('../Files'):
    print(file_info)
