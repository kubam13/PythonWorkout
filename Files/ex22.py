import csv


def passwd_to_csv(read_file, write_file):
    with open(read_file, 'r') as csv_file_read:
        with open(write_file, 'w', newline='') as csv_file_write:
            csv_reader = csv.reader(csv_file_read, delimiter=':')
            csv_writer = csv.writer(csv_file_write, delimiter='\t')
            for line in csv_reader:
                try:
                    csv_writer.writerow([line[0], line[2]])
                except IndexError:
                    pass


passwd_to_csv('user_database_short.txt', 'user_database_result.txt')