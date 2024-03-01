import csv

sample_dict = {'a': 1, 'b': 2, 'c': 'tak'}


def dict_to_csv(dictionary, write_file):
    with open(write_file, 'w') as csv_file_write:
        csv_writer = csv.writer(csv_file_write, delimiter='\t')
        for key, value in dictionary.items():
            csv_writer.writerow([key, value, type(value).__name__])


dict_to_csv(sample_dict, 'dict_to_csv_result.txt')
