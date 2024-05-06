from collections import Counter


class Repeat:
    def __init__(self, words):
        self.words = words

    def find_word(self):
        max_list = []

        for word in self.words:
            max_list.append(max(dict(Counter(word)).values()))

        for word in self.words:
            if max(dict(Counter(word)).values()) == max(max_list):
                return word

    def find_word_vowels(self):

        vowels_list = []
        max_list = []
        for word in self.words:
            result = [letter for letter in word if letter in 'aeiou']
            result = ''.join(result)
            vowels_list.append(result)

        for vowels in vowels_list:
            max_list.append(max(dict(Counter(vowels)).values()))

        for vowels in vowels_list:
            if max(dict(Counter(vowels)).values()) == max(max_list):
                idx = vowels_list.index(vowels)

        return self.words[idx]


words = Repeat(['this', 'is', 'an', 'elementary', 'testtest', 'example'])


print(words.find_word())
print(words.find_word_vowels())