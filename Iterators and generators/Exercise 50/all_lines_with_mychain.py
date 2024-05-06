import os


def mychain(*args):
    for arg in args:
        for item in arg:
            yield item.strip('\n')


def all_lines(path):
    return mychain(*(open(os.path.join(path, filename))
                          for filename in os.listdir(path)))


for i in all_lines('../Files'):
    print(i)