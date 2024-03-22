def get_sv(file):
    vowels = {'a','e','i','u','o'}
    with open(file,'r') as text:
        return {word.strip() for word in text if vowels <= set(word.lower())}


print(get_sv('words.txt'))
