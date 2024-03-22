import random


def create_password_generator(symbols_string):
    def create_password(integer):
        password = []
        for _ in range(integer):
            password.append(random.choice(symbols_string))
        return ''.join(password)
    return create_password


alpha_password = create_password_generator('abcde12345')
print(alpha_password(7))