import os


def files():
    files_dict = {}
    names = os.listdir()
    for name in names:
        files_dict[name] = os.stat(name).st_size
    return files_dict


print(files())