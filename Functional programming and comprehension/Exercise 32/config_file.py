def config_file(config):
    with open(config,'r') as read_text:
        config_dict = {line.split('=')[0]: line.split('=')[1].strip() for line in read_text}
        return config_dict


print(config_file('config_file.txt'))