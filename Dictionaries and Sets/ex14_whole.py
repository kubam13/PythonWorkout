from datetime import date


class Exercise14:
    def __init__(self, variable):
        self.variable = variable

    def restaurant(self):
        total_cost = 0
        order = input('Order: ')
        while order != '':
            if order in self.variable.keys():
                total_cost += self.variable[order]
                print(f"{order} costs {self.variable[order]}, total is {total_cost}")
            else:
                print(f'Sorry, we are fresh out of {order} today.')
            order = input('Order: ')
        print(f'Your total is {total_cost}')

    def login(self):
        username = input('Username: ')
        password = input('Password: ')
        if username in self.variable.keys() and password in self.variable.values():
            if password == self.variable[username]:
                return f'Hello {username} you are logged in.'
            else:
                return f'Password or username is incorrect. Please try again.'
        else:
            return f'Password or username is incorrect. Please try again.'

    def get_temperature(self):
        day = input('Enter a date: ')
        for i in self.variable.keys():
            if day == i:
                print(f'Dzisiejsza temperatura to {self.variable[day]}.')
                if list(self.variable.keys()).index(i) == 0:
                    print('Brak danych o wczorajszej temperaturze.')
                else:
                    print(
                        f'Wczorajsza temperatura wynosila {self.variable[list(self.variable.keys())[list(self.variable.keys()).index(i) - 1]]}.')
                try:
                    print(f'A jutrzejsza bedzie wynosic {self.variable[list(self.variable.keys())[list(self.variable.keys()).index(i) + 1]]}')
                except IndexError:
                    print('Brak danych o jutrzejszej temperaturze.')

    def how_many_days(self):
        who = input('Enter name: ')
        delta = date.today() - self.variable[who.lower()]
        return f'{who} zyje juz {delta.days} dni.'


MENU = Exercise14({'hot dog': 10, 'pizza': 24, 'butter chicken': 31, 'fries': 5, 'tea': 8, 'beer': 11})
USERS = Exercise14({'hot dog man': 'ilovehotdogs3', 'the dude': 'lebowski', 'butter': 'butter', 'idiot': 'password'})
DAYS = Exercise14({'28.01': '1 stopien C', '29.01': '3 stopnie C', '30.01': '10 stopni C', '31.01': '-8 stopni C'})
BIRTHDAYS = Exercise14({'michal': date(1969,3,25), 'kasia': date(1967,5,12), 'kamil': date(1998,2,18), 'kuba': date(1994,11,25)})

#MENU.restaurant()
#print(USERS.login())
#DAYS.get_temperature()
print(BIRTHDAYS.how_many_days())
