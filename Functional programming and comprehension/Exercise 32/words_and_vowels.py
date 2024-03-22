def words_and_vowels(sentence):
    vowels = 'aeiou'
    dict_with_vowels = {word: sum((word.lower().count(vowel)) for vowel in vowels) for word in sentence.split()}
    return dict_with_vowels


my_string = 'THIS is an easy test'
print(words_and_vowels(my_string))