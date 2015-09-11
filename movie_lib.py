import csv
all_movies = {}
all_users = {}

class Movie:

    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {} #key: user_id, value: Rating objects

    def add_rating(self, rating): #rating is an instance of CLASS rating.
        self.ratings[rating.user] = rating.score

    def __str__(self):
        return 'Movie({}, {})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()

    def get_movie_ratings(self):
        return sorted(self.ratings.values(),reverse=True)

    def get_average_rating(self):
        '''Takes a movie id and returns the average of all the ratings'''
        return sum(self.get_movie_ratings())/len(self.get_movie_ratings())

    def get_movie_title(self):
        '''Takes a movie_id and returns the movie title.'''
        return all_movies[self.id].title
class Rating:

    def __init__(self,user, movie, score):
        self.score = score
        self.user = user
        self.movie = movie
        all_movies[self.movie].add_rating(self)
        all_users[self.user].add_user_rating(self)

    # def __str__(self):
    #     return 'Rating(user={}, movie={}, score={})'.format(self.user, self.movie, self.score)
    #
    # def __repr__(self):
    #     return self.__str__


class User:

    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self
        self.ratings = {} #Key Movie_id, value rating score

    def add_user_rating(self, rating): #Rating is an instance of the CLASS rating
        self.ratings[rating.movie] = rating.score

    def get_user_ratings(self):
        return self.ratings

with open('u.item', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title'], delimiter='|')
    for row in reader:
        Movie(int(row['movie_id']), row['movie_title'])
with open('u.user') as f:
    reader = csv.DictReader(f, fieldnames=['user_id'], delimiter='|')
    for row in reader:
        User(int(row['user_id']))

with open('u.data') as f:
    reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating'], delimiter='\t')
    for row in reader:
        Rating(int(row['user_id']), int(row['movie_id']), int(row['rating']))

def get_top_50(all_movies=all_movies):
    top_movies = {}
    for key in all_movies:
        if len(all_movies[key].get_movie_ratings()) > 10:
            top_movies[key] = all_movies[key].get_average_rating()
    top_movies = sorted(top_movies.items(), key=lambda c: c[1], reverse=True)
    print(top_movies[:50])



def get_user_suggest(user, all_movies=all_movies, all_users=all_users):
    safe_dict = all_movies.copy()
    for key in all_users[user].ratings:
        del safe_dict[key]
    get_top_50(safe_dict)
