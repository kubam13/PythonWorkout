import shutil


def copyfile(file, *args):
    for arg in args:
        shutil.copyfile(file, arg)


copyfile('sample.txt', 'copy1.txt')