import json
import csv


def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as csvfile:
        csv_data = csv.reader(csvfile)

        data_list = [tuple(row) for row in csv_data]

    with open(json_file, 'w') as jsonfile:
        json.dump(data_list, jsonfile)


csv_to_json('user_database_short.txt', 'sample.json')