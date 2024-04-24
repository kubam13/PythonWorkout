my_currencies = {'zloty': 0.25, 'euro': 1.08, 'korona': 0.043, 'frank': 1.1}


def currency_prices(currencies):
    your_currency = input('What is your currency? ')
    return {key: round(value/currencies[your_currency], 2) for key, value in currencies.items()}


print(currency_prices(my_currencies))
