def shells(file):
    text = open(file, 'r')
    shells_dict = {}
    for line in text:
        if line.split(':')[-1] not in shells_dict.keys():
            shells_dict[line.split(':')[-1]] = [line.split(':')[0]]
        else:
            shells_dict[line.split(':')[-1]].append(line.split(':')[0])
    return shells_dict


print(shells('user_database.txt'))