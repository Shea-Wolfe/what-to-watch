class Movie():

    def __init__(self, movie_id):
        self.movie_id = movie_id


    def get_rating(self):
        '''Should be able to take a movie_id and return the ratings'''
        movie_ratings = []
        for rating in ratings_list:
            if rating[1] == self.movie_id:
            movie_ratings.append(rating[2])
        return movie_ratings

    def get_average_rating(self):
        '''Takes a movie id and returns the average of all the ratings'''
        return sum(get_rating(movie_id))/len(get_rating/movie_id)

    def get_movie_title(self):
        '''Takes a movie_id and returns the movie title.'''
        return movie_list[self.movie_id]
class Rating:

    def __init__(self,user_id, movie_id, rating):
        self.rating = rating
        self.user_id = user_id
        self.movie_id = movie_id

class User():

    def __init__(self, rating, user_id):
        (rating, user_id)

    def get_user_ratings(self):
        '''takes a user_id and returns all the ratings done by that user'''
