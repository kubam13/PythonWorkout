def encrypt(read_file, text_to_numbers, numbers_to_txt):
    with open(read_file, 'r') as read_text, open (text_to_numbers, 'w') as write_numbers:
        for line in read_text:
            for element in line:
                write_numbers.write(str(ord(element))+' ')

    with open(text_to_numbers, 'r') as read_text, open (numbers_to_txt, 'w') as write_text:
        for line in read_text:
            for element in line.strip().split():
                write_text.write(chr(int(element)))


encrypt('ex24.txt', 'write_encrypted_numbers.txt','write_encrypted_text.txt')