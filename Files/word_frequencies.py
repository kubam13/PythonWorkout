def word_frequencies():
    var = input('Enter text file name and words to count: ')
    word_list = []
    word_dict = {}
    with open(var.split()[0], 'r') as text:
        for line in text:
            for word in line.strip().split():
                word_list.append(word)

        for i in var.split()[1:]:
            word_dict[i] = word_list.count(i)

        return word_dict


print(word_frequencies())