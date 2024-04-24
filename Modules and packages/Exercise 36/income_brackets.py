def income_brackets(income):
    income = int(income)
    if income <= 1000:
        tax = 0
    elif 1000 > income >= 10000:
        tax = 0.1 * (income - 1000)
    elif 10000 > income >= 20000:
        tax = 1000 + 0.2*(income - 10000)
    else:
        tax = 3000 + 0.5*(income - 20000)
    return tax

