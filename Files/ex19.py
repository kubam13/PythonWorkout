def passwd_to_dict(file):
    text = open(file, 'r')
    pass_dict = {}
    for line in text:
        pass_dict[line.split(':')[0]] = line.split(':')[2]
    return pass_dict


print(passwd_to_dict('user_database.txt'))