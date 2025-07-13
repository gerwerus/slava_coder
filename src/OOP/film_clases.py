# Напишите класс для программы, которая работает с фильмами.
# У фильма должны быть: название, режиссер и год, когда этот фильм был впервые показан.
# Напишите метод, который будет выводить информацию о фильме.
# Создайте несколько экземпляров класса с вашими любимыми фильмами.
# Положите их в массив. И с помощью цикла выведите информацию о фильмах.


class Movie:
    def __init__(self, title: str, director: str, year_show: int) -> None:
        self.title = title
        self.director = director
        self.year_show = year_show

    def get_info(self) -> None:
        movie_favorite_array = [self.title, self.director, self.year_show]
        for atribute in movie_favorite_array:
            print(atribute)


movie_favorite_one = Movie('Иллюзия обмана', 'Louis Leterrier', 2010)
movie_favorite_two = Movie('Социальная сеть', 'David Fincher', 2010)
movie_favorite_three = Movie('Бойцовский клуб', 'David Fincher', 1999)
movie_favorite_array_all = [movie_favorite_one, movie_favorite_two, movie_favorite_three]
for movie in movie_favorite_array_all:
    movie.get_info()
