def config_to_dict(config):
    return {line.split('=')[0]: int(line.split('=')[1].strip())
            for line in open(config) if line.split('=')[1].strip().isdigit()}


print(config_to_dict('config.txt'))