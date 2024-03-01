import os

import hashlib


def names_to_md5(directory):

    names = os.listdir(directory)
    for name in names:
        full_path = os.path.join(directory, name)
        result = hashlib.md5(full_path.encode())
        print(f'{full_path}: {result.hexdigest()}')


names_to_md5('directory for texts')