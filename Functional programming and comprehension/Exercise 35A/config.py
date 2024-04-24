def config_to_dict(config):
    return {line.split('=')[0]:line.split('=')[1].strip() for line in open(config)}


print(config_to_dict('config.txt'))