import re


def response_code_sum():
    ip_adresses = {}

    with open('apache.txt', 'r') as file:
        for line in file:
            code = re.search(r'\s\d{3}\s', line).group()
            ip = re.match(r'\d+\.\d+\.\d+\.\d+', line).group()

            if code in ip_adresses:
                ip_adresses[code].append(ip)
            else:
                ip_adresses[code] = [ip]

        codes_sum = {i: len(ip_adresses[i]) for i in ip_adresses.keys()}

        print(codes_sum)


response_code_sum()