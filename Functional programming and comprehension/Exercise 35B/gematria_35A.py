import string


def gematria():
    return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}