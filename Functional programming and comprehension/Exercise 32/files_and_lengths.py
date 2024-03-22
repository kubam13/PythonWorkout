import os


def files_and_lengths(directory):
    files_and_lengths_dict = {file: os.stat(os.path.join(directory, file)).st_size for file in os.listdir(directory)}
    return files_and_lengths_dict


print(files_and_lengths('../Exercise 29'))