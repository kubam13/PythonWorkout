def get_shells(file):
    return {line.split(':')[-1].strip() for line in open(file)}


print(get_shells('../../Files/user_database.txt'))
