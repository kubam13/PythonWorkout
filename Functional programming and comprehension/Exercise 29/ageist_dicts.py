list_of_people = [{'name':'James','age':31}, {'name':'Mariola','age':12}, {'name':'Mario','age':55},
                  {'name':'Luigi','age':20}, {'name':'Harry','age':19}]


def ageist_function(people):
    new_list = [{'name': person['name'], 'age': person['age'],'age in months': person['age']*12}
                for person in people
                if person['age']<=20]
    print(new_list)


ageist_function(list_of_people)
