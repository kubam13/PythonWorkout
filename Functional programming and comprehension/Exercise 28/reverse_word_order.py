def reverse_word_order(text):
    with open(text,'r') as read_text:
        return [' '.join(line.split()[::-1]) for line in read_text]


print(reverse_word_order('../../Files/ex24.txt'))