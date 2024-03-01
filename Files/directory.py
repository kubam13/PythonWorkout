import os


def letters_in_files():
    letters_dict = {}
    names = os.listdir()
    for name in names:
        with open(name, 'r') as text:
            for line in text:
                for char in line:
                    if char.isalpha():
                        if char.lower() not in letters_dict.keys():
                            count = 1
                            letters_dict[char.lower()] = count
                        else:
                            count += 1
                            letters_dict[char.lower()] = count
                    else:
                        pass

    return dict(sorted(letters_dict.items()))


print(letters_in_files())