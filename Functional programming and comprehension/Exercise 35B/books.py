def books_comprehension(books_list):
    return{book[1]: {'author first name': book[0].split()[0],
                     'author last name': book[0].split()[1],
                     'price': book[2]}
           for book in books_list}


books = [('George Martin', 'Gra o tron', 15),('Joanne Rowling', 'Harry Potter', 10),
         ('Dan Simmons', 'Upadek Hyperiona', 11)]

print(books_comprehension(books))