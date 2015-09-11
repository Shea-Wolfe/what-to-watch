class Movie:

    def __init__(self, movie_id):
        self.movie_id = movie_id


    def get_rating(self):
        '''Should be able to take a movie_id and return the ratings'''
        ratings_list = [['Will', 42, 3],['Steve', 47, 5]]
        movie_ratings = []
        for rating in ratings_list:
            if rating[1] == self.movie_id:
                movie_ratings.append(rating[2])
        return movie_ratings

    def get_average_rating(self):
        '''Takes a movie id and returns the average of all the ratings'''
        return sum(self.get_rating())/len(self.get_rating())

    def get_movie_title(self):
        '''Takes a movie_id and returns the movie title.'''
        movie_list = {42: "Star Wars", 47: 'Star Trek'}
        return movie_list[self.movie_id]
class Rating:

    def __init__(self,user_id, movie_id, rating):
        self.rating = rating
        self.user_id = user_id
        self.movie_id = movie_id



class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_ratings(self):
        '''takes a user_id and returns all the ratings done by that user'''
        user_ratings = []
        ratings_list = [['Will', 42, 3],['Steve', 47, 5]]
        for rating in ratings_list:
            if rating[0] == self.user_id:
                user_ratings.append([rating[1],rating[2]])
        return user_ratings
