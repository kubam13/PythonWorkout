a = 1
b = 2
c = 3


def foo(var):
    return [var]


def bar(var):
    return int(var) + 1


__all__ = ['a', 'c', 'bar']