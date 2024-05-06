def my_chain(*args):
    for arg in args:
        for item in arg:
            yield item

if __name__ == '__main__':
    for i in my_chain('abc', [1, 2, 3], {'a': 1, 'b': 2}):
        print(i)
