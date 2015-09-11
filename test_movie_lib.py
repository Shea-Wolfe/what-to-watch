from movie_lib import *
will = User('Will')
movie = Movie(42)

def test_get_rating():
    assert movie.get_rating() == [3]

def test_get_average_rating():
    assert movie.get_average_rating() == 3

def test_get_movie_title():
    assert movie.get_movie_title() == 'Star Wars'

def test_get_user_ratings():
    assert will.get_user_ratings() == [[42,3]]
