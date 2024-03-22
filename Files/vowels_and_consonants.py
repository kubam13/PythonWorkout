import string


def separate_vowels_and_consonants(read_file, vowels, consonants):
    with open(read_file, 'r') as read_text, open (vowels, 'w') as write_vowels, open(consonants,'w') as write_consonants:
        for line in read_text:
            for element in line:
                if element in 'aeiou':
                    write_vowels.write(element.strip())
                elif element in string.punctuation:
                    pass
                else:
                    write_consonants.write(element.strip())
            write_vowels.write('\n')
            write_consonants.write('\n')


separate_vowels_and_consonants('second_sample.txt', 'vowels.txt','consonants.txt')