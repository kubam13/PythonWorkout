import json
import csv


def file_to_dict(csv_file, json_file):
    data_list = []
    with open(csv_file, 'r') as csvfile:
        csv_data = csv.reader(csvfile, delimiter=':')

        for row in csv_data:
            if not row[0].startswith("#"):
                result_dict = {
                    'username': row[0],
                    'encrypted': row[1],
                    'uid': row[2],
                    'gid': row[3],
                    'gecos': row[7],
                    'home directory': row[8],
                    'shell': row[9],
                }
                data_list.append(result_dict)
            else:
                pass

    with open(json_file, 'w') as jsonfile:
        json.dump(data_list, jsonfile)


file_to_dict('user_database_short.txt', 'sample.json')