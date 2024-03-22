def vowel_and_characters(text):
    with open(text,'r') as read_text:
        proper_list = [line for line in read_text if len(list(line))>20 and any(char.lower() in 'aeiou' for char in line)]
        for element in proper_list:
            print(element.strip())


vowel_and_characters('../../Files/second_sample.txt')