from collections import namedtuple


class Records:
    def __init__(self, records):
        self.records = records

    def format_sort_records(self):
        formatted_records = []
        for i in self.records:
            formatted_records.append(f"{i[1]:<10} {i[0]:<10} {'%.2f' % i[2]:<5}")
        return "\n".join(formatted_records)

    def format_sort_records_by_names(self):
        formatted_records = []
        for record in self.records:
            Point = namedtuple('Point', ['name', 'surname', 'distance'])
            point = Point(name=0, surname=1, distance=2)
            formatted_records.append(
                f"{record[point.surname]:<10} {record[point.name]:<10} {'%.2f' % record[point.distance]:<5}")
        return "\n".join(formatted_records)


class Movies:
    def __init__(self, movies):
        self.movies = movies

    def sort_movies(self):
        way_of_sort = input("How would you like to sort?[name of the movie, length, director name] ")
        if way_of_sort == 'name of the movie':
            return sorted(self.movies)
        elif way_of_sort == 'length':
            return sorted(self.movies, key=lambda x: x[1])
        elif way_of_sort == 'director name':
            return sorted(self.movies, key=lambda x: x[2])
        else:
            return ('Invalid input')

    def sort_movies_by_multiple(self):
        way_of_sort = input("How would you like to sort?[name of the movie, length, director name] ").split(", ")
        if all(x in ['name of the movie', 'length', 'director name'] for x in way_of_sort):
            if 'name of the movie' in way_of_sort:
                self.movies = sorted(self.movies)
                if 'length' in way_of_sort:
                    self.movies = sorted(self.movies, key=lambda x: x[1])
                    if 'director name' in way_of_sort:
                        self.movies = sorted(self.movies, key=lambda x: x[2])
            return self.movies
        else:
            return ('Invalid input')


people = Records([('Donald', 'Trump', 7.85), ('Jinping', 'Xi', 10.603), ('Vladimir', 'Putin', 3.626)])
movies = Movies([('Everything Everywhere All at Once', 140, 'Dan Kwan'), ('Avatar: The Way of Water', 192, 'James Cameron'), ('The Banshees of Inisherin', 114, 'Martin McDonagh'), ('Elvis',159,'Baz Luhrmann'), ('Top Gun: Maverick',131,'Joseph Kosinski')])

# print(people.format_sort_records())
# print(people.format_sort_records_by_names())
# print(Movies.sort_movies(movies))
print(movies.sort_movies_by_multiple())
