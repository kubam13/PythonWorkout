def characters(input_string):
    characters_dict = dict.fromkeys(('isdigit', 'isalpha','isspace'),0)
    for letter in input_string:
        if letter.isdigit():
            characters_dict['isdigit'] += 1
        elif letter.isalpha():
            characters_dict['isalpha'] += 1
        elif letter.isspace():
            characters_dict['isspace'] += 1
        else:
            pass
    return characters_dict



