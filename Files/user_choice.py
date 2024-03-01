import csv


def passwd_to_csv(read_file, write_file):
    fields = input('Which fields should be written to CSV? '
                   'Put integers in range 0-9 separated by whitespaces: ')
    fields_list = [int(field) for field in fields.split()]
    limiter = input('Which character should be used as a delimiter? ')
    with open(read_file, 'r') as csv_file_read:
        with open(write_file, 'w', newline='') as csv_file_write:
            csv_reader = csv.reader(csv_file_read, delimiter=':')
            csv_writer = csv.writer(csv_file_write, delimiter=limiter)
            for line in csv_reader:
                try:
                    csv_writer.writerow([line[idx] for idx in fields_list])
                except IndexError:
                    pass


passwd_to_csv('user_database_short.txt', 'user_database_result.txt')