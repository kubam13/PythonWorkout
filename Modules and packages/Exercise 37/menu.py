def menu(**kwargs):
    user_choices_string = '/'.join(sorted(kwargs))
    user_choice = input(f'Choose an option {user_choices_string}: ')
    if user_choice in kwargs:
        return kwargs[user_choice]()
    else:
        return f'{user_choice} is not a valid option'
