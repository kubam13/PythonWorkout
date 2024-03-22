import string


def password_checker(password):
    min_uppercase = 1
    min_lowercase = 1
    min_punctuation = 1
    min_digit = 1
    total_uppercase = sum(i.isupper() for i in password)
    total_lowercase = sum(i.islower() for i in password)
    total_punctuation = sum(1 for i in password if i in string.punctuation)
    total_digit = sum(i.isdigit() for i in password)
    if total_uppercase < min_uppercase:
        print(f'You need to have at least {min_uppercase} uppercases in your password.')
    if total_lowercase < min_lowercase:
        print(f'You need to have at least {min_lowercase} lowercases in your password.')
    if total_punctuation < min_punctuation:
        print(f'You need to have at least {min_punctuation} punctuation in your password.')
    if total_digit < min_digit:
        print(f'You need to have at least {min_digit} digit in your password.')
    if (total_uppercase >= min_uppercase and total_lowercase >= min_lowercase
            and total_punctuation >= min_punctuation and total_digit >= min_digit):
        print('Password valid')


password_checker(input('Whats your password? '))