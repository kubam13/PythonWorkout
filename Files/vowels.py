def how_many_vowels(file):
    vowels_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    text = open(file, 'r')
    for line in text:
        for char in line:
            if char in vowels_dict.keys():
                vowels_dict[char] +=1

    return vowels_dict


print(how_many_vowels('sample.txt'))