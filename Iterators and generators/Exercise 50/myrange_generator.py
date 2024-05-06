def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while start < stop:
        yield start
        start += step


for i in my_range(7):
    print(i)

