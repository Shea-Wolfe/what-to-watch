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
        return 'Movie(movie_id={}, title={})'.format(self.id, __repr__(self.title))

    def __repr__(self):
        return self.__str__

    # def get_rating(self):
    #
    #
    # def get_average_rating(self):
    #     '''Takes a movie id and returns the average of all the ratings'''

    def get_movie_title(self):
        '''Takes a movie_id and returns the movie title.'''
        return self.title
# class Rating:
#
#     def __init__(self,user, movie, score):
#         self.score = score
#         self.user = user
#         self.movie = movie
#         all_movies[self.movie].add_rating(self)
#         all_users[self.user].add_user_rating(self)
#
#     def __str__(self):
#         return 'Rating(user={}, movie={}, score={})'.format(self.user, self.movie, self.score))
#
#     def __repr__(self):
#         return self.__str__


class User:

    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self
        self.ratings = {} #Key Movie_id, value rating score

    def add_user_rating(self, rating): #Rating is an instance of the CLASS rating
        self.ratings[rating.movie] = rating.score


    # def get_user_ratings(self):
    #     '''takes a user_id and returns all the ratings done by that user'''
    #     user_ratings = []
    #     ratings_list = [['Will', 42, 3],['Steve', 47, 5]]
    #     for rating in ratings_list:
    #         if rating[0] == self.user_id:
    #             user_ratings.append([rating[1],rating[2]])
    #     return user_ratings
