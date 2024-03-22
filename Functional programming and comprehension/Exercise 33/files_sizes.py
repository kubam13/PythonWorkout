import os


def files_sizes(directory):
    return {file: os.stat(os.path.join(directory, file)).st_size for file in os.listdir(directory)}


print(files_sizes('../Exercise 29'))