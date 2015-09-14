import csv
import math
from random import randint, choice
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

def get_items():
    with open('u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title'], delimiter='|')
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

def get_users():
    with open('u.user') as f:
        reader = csv.DictReader(f, fieldnames=['user_id'], delimiter='|')
        for row in reader:
            User(int(row['user_id']))

def get_data():
    with open('u.data') as f:
        reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'rating'], delimiter='\t')
        for row in reader:
            Rating(int(row['user_id']), int(row['movie_id']), int(row['rating']))

def get_top_x(num=50, all_movies=all_movies):
    top_movies = {}
    for key in all_movies:
        if len(all_movies[key].get_movie_ratings()) > 10:
            top_movies[key] = all_movies[key].get_average_rating()
    top_movies = sorted(top_movies.items(), key=lambda c: c[1], reverse=True)
    return top_movies[:num]

def get_user_suggest(user, all_movies=all_movies, all_users=all_users):
    safe_dict = all_movies.copy()
    for key in all_users[user].ratings:
        del safe_dict[key]
    movie_suggested = get_top_x(5, safe_dict)
    return all_movies[movie_suggested[randint(0,4)][0]].title

def euclidean_distance(v, w): #Formula copied from James Allen
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    if len(v) is 0:
        return 0
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))


def compare_users(user1, user2, all_users=all_users):
    user1_scores = []
    user2_scores = []
    for key in all_users[user1].ratings:
        if key in all_users[user2].ratings:
            user1_scores.append(all_users[user1].ratings[key])
            user2_scores.append(all_users[user2].ratings[key])
    if len(user1_scores) < 10:
        return 0
    return euclidean_distance(user1_scores,user2_scores)

def get_unshared_movies(p_user, s_user, all_users=all_users, all_movies=all_movies):
    '''takes a primary user and a secondary user.  Returns a list of movies that
    the secondary user has seen but the primary user hasn't'''
    s_user_list = []
    s_user_movie_dict = {}
    for key in all_users[s_user].ratings:
        if key not in all_users[p_user].ratings:
            s_user_movie_dict[key] = all_movies[key]
    return (s_user_movie_dict, s_user)

def find_similar_user(user1, all_users=all_users, all_movies=all_movies):
    sim = 0.20
    store_users = []
    for user in all_users:
        if user1 == user:
            pass
        elif compare_users(user1, user) > sim:
            store_users.append((user, compare_users(user1, user)))
    return (store_users, user1)

def store_user_picks(user_list, all_movies=all_movies):
    user_list_split, user1 = user_list
    movie_pick = []
    test_weight = 0
    for user in user_list_split:
        un_weight = get_user_fav_movie(get_unshared_movies(user1, user[0]))
        weight = all_movies[un_weight].get_average_rating() * user[1]
        if weight > test_weight:
            movie_pick = un_weight
    return all_movies[movie_pick].title

def get_user_fav_movie(suggestion_list, all_users=all_users):
    suggestion_list, user = suggestion_list
    new_dict = {}
    for key in suggestion_list:
        new_dict[key] = all_users[user].get_user_ratings()[key]
    sorted_dict = sorted(new_dict.items(), key=lambda c: c[1], reverse=True)
    sorted_dict = sorted_dict[:5]
    return sorted_dict[randint(0,4)][0]
