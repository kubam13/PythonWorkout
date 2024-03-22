def unix_dict(file):
    with open(file,'r') as read_text:
        return {line.split(':')[0]: line.split(':')[2] for line in read_text if not line.startswith('#')}


print(unix_dict('../../Files/user_database_short.txt'))