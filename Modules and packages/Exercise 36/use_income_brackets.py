from income_brackets import income_brackets

salary = input('What is your income? ')
print(f'Your tax is: {income_brackets(salary)}')