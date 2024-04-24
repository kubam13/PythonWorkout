import gematria_35A

gematria_dict = gematria_35A.gematria()


def gematria_for(word):
    return sum(gematria_dict.get(letter, 0) for letter in word)


def gematria_equal_words(my_word):
    return [word.strip() for word in open('../Exercise 34/words.txt')
            if gematria_for(word) == gematria_for(my_word)]


print(gematria_for('cat'))
print(gematria_equal_words('cat'))