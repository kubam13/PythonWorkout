import time


def elapsed_since(data, min_time):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        if delta > min_time:
            last_time = time.perf_counter()
            yield (delta, item)
        else:
            time.sleep(min_time-delta)
            last_time = time.perf_counter()
            yield (delta, item)


for i in elapsed_since('abcd', 2):
    print(i)