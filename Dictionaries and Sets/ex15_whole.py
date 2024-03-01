import re


class Exercise15:

    @staticmethod
    def get_rainfall():
        rainfall = {}
        city = input('Enter city: ')
        while city != '':
            rain = input('How much rain? ')
            if city in rainfall.keys():
                rainfall[city] = int(rainfall[city]) + int(rain)
            else:
                rainfall.update({city: rain})
            city = input('Enter city: ')
        for key, value in rainfall.items():
            print(f'{key} : {value}')

    @staticmethod
    def get_rainfall_avg():
        rainfall = {}
        city = input('Enter city: ')
        while city != '':
            rain = input('How much rain? ')
            if city not in rainfall.keys():
                count = 1
                total_rain = int(rain)
                rainfall.update({city: {total_rain: count}})
            else:
                count += 1
                total_rain += int(rain)
                rainfall[city] = {total_rain: count}
            city = input('Enter city: ')

        for key, value in rainfall.items():
            for second_key, second_value in value.items():
                print(
                    f'In {key} total rainfall was: {second_key} and average rainfall was: {second_key / second_value}.')

    @staticmethod
    def create_ip_list():
        ip_adresses = {}

        with open('apache.txt', 'r') as file:
            for line in file:
                code = re.search(r'\s\d{3}\s', line).group()
                ip = re.match(r'\d+\.\d+\.\d+\.\d+', line).group()

                if code in ip_adresses:
                    ip_adresses[code].append(ip)
                else:
                    ip_adresses[code] = [ip]
        print(ip_adresses)

    @staticmethod
    def words_length():
        with open("sample.txt", "r") as file:
            text = file.read()
            words_list = text.split()
            length_dict = {}
            for word in words_list:
                word_length = len(word)
                if word_length in length_dict.keys():
                    count += 1
                    length_dict.update({word_length: count})
                else:
                    count = 1
                    length_dict.update({word_length: count})

            for key, value in sorted(length_dict.items()):
                if value == 1:
                    print(f'There is {value} {key}-letters word in text.')
                else:
                    print(f'There are {value} of {key}-letters words in text.')


#Exercise15.get_rainfall()
#Exercise15.get_rainfall_avg()
Exercise15.create_ip_list()
#Exercise15.words_length()
