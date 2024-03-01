import json
import glob


def print_scores(directory):
    result_dict = {}
    for filename in glob.glob(f'{directory}/*.json'):
        result_dict[filename] = {}

        with open(filename) as file:
            json_data = json.load(file)

            for single_dict in json_data:
                for key, value in single_dict.items():
                    result_dict[filename][key] = result_dict[filename].get(key, []) + [value]

            print(filename)
            for key, value in reversed(result_dict[filename].items()):
                print(f'{key}: min {min(value)}, max {max(value)}, average {sum(value)/len(value)}')


print_scores('scores')