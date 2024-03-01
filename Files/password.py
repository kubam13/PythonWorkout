def passwd_to_dict(file):
    with open(file, 'r') as text:
        pass_dict = {}
        for line in text:
            pass_dict[line.split(':')[0]] = \
                {'user ID': line.split(':')[2],
                 'home directory': line.split(':')[-2],
                 'shell': line.split(':')[-1].strip('\n')}
        return pass_dict


print(passwd_to_dict('user_database.txt'))