def word_count(file):
    with open(file, 'r') as text:
        line_count = 0
        list_of_words = []
        char_count = 0
        for line in text:
            line_count += 1
            char_count += len(line)
            for word in line.split():
                list_of_words.append(word)
    return f'There are {char_count} characters, {len(list_of_words)} words, {line_count} lines ' \
           f'and {len(set(list_of_words))} unique words.'


print(word_count('second_sample.txt'))