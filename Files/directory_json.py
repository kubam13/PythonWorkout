import json
import os


def directory_json(json_file):
    directory = input('Directory name: ')
    directories_info = []
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        directory_info = {
            'filename': file,
            'file size': os.stat(path).st_size,
            'last modified': os.stat(path).st_mtime
             }
        directories_info.append(directory_info)

    with open(json_file, 'w') as jsonfile:
        json.dump(directories_info, jsonfile)

    with open(json_file) as jsonfile:
        json_data = json.load(jsonfile)
        size_dict = {}
        modification_time_dict = {}
        for file in json_data:
            size_dict[file['filename']] = [file['file size']]
            modification_time_dict[file['filename']] = [file['last modified']]
            min_size_key = min(size_dict, key=size_dict.get)
            max_size_key = max(size_dict, key=size_dict.get)
            min_time_key = min(modification_time_dict, key=modification_time_dict.get)
            max_time_key = max(modification_time_dict, key=modification_time_dict.get)

        print(f'Last modified was file {min_time_key} and most recently {max_time_key}.'
              f' File {max_size_key} has the biggest size and {min_size_key} is the smallest.')


directory_json('Directories_data.json')