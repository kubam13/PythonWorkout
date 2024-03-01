import os
import arrow


def creation_time():
    directory = input('Enter directory name: ')
    names = os.listdir(directory)
    for name in names:
        full_path = os.path.join(directory, name)
        date = arrow.Arrow.fromtimestamp(os.stat(full_path).st_ctime)
        print(date)


creation_time()
