import re
import os


class Exercise17:
    def __init__(self, numbers):
        self.numbers = numbers

    def how_many_different_numbers(self):
        set_of_numbers = set(self.numbers)
        count = 0
        for _ in set_of_numbers:
            count += 1
        print(count)

    @staticmethod
    def different_ip():
        ip = set()

        with open('apache.txt', 'r') as file:
            for line in file:
                pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
                one_ip = pattern.match(line)
                ip.add(one_ip.group())
            print(ip)

    @staticmethod
    def different_response_codes():
        response_codes = set()

        with open('apache.txt', 'r') as file:
            for line in file:
                pattern = re.compile(r'\s\d{3}\s')
                code = pattern.search(line)
                response_codes.add(code.group().strip())
            print(response_codes)

    @staticmethod
    def names_in_directory():
        set_of_extensions = set()
        names = os.listdir()
        for name in names:
            file_name, file_extension = os.path.splitext(name)
            set_of_extensions.add(file_extension)
        print(names, set_of_extensions)


NUMBERS = Exercise17([1, 2, 3, 1, 2, 3, 4, 1, 5, 7, 5])

#NUMBERS.how_many_different_numbers()
Exercise17.different_ip()
#Exercise17.different_response_codes()
#Exercise17.names_in_directory()


