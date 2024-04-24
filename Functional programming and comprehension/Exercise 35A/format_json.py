import json


def format_json(json_file):
    return {single_dict["city"]: single_dict["population"] for single_dict in json.load(open(json_file))}


def format_json_with_tuples(json_file):
    return {(single_dict["city"], single_dict["state"]): single_dict["population"]
            for single_dict in json.load(open(json_file))}


# print(format_json("cities.json"))
# print(len(format_json("cities.json")))
print(format_json_with_tuples("cities.json"))
print(len(format_json_with_tuples("cities.json")))