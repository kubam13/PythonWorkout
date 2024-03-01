import csv
import random


def sum_and_mean():
    text_file = input('Enter file name: ')
    with open(text_file, 'w', newline='') as csv_file_write:
        csv_writer = csv.writer(csv_file_write)
        rows = [[random.randint(10, 100) for _ in range(10)] for _ in range(4)]
        csv_writer.writerows(rows)

    with open(text_file, 'r') as csv_file_read:
        csv_reader = csv.reader(csv_file_read)
        for row in csv_reader:
            int_row = [int(element) for element in row]
            print(sum(int_row), sum(int_row)/len(int_row))


sum_and_mean()