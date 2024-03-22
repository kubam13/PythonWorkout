def pig_latin_word(word):
    if word[0] in 'aeiou':
        return word+'way'
    else:
        return word[1:]+word[0]+'ay'


def pig_latin_translation(filename):
    return ' '.join(pig_latin_word(word) for line in open(filename) for word in line.split())


print(pig_latin_translation('../../Files/second_sample.txt'))