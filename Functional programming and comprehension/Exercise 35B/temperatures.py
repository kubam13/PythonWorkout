def fahrenheit_to_celsius(temp_dict):
    return {key: round(5/9*(value-32), 1) for key, value in temp_dict.items()}


cities = {'Szczecin': 112, 'NY': 83, 'WWA': 90, 'Boston': 60}
print(fahrenheit_to_celsius(cities))