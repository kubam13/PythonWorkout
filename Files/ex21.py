import os


def find_longest(file):
    with open(file, 'r') as text:
        word_list = []
        for line in text:
            for word in line.split():
                word_list.append(word.strip('.'))
        longest = max(word_list, key=len)
    return longest


def all_longest_words(directory):
    names = os.listdir(directory)
    longest_list = []
    for name in names:
        full_path = os.path.join(directory, name)
        longest_list.append(find_longest(full_path))
    return max(longest_list, key=len)


print(find_longest('second_sample.txt'))
print(all_longest_words('Files'))