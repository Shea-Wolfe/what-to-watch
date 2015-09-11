from movie_lib import *


def test_get_rating():
    assert get_rating(42) == [3]

def test_get_average_rating():
    assert get_average_rating(42) == 3

def test_get_movie_title():
    assert get_movie_title(42) == 'Star Wars'

def test_get_user_ratings():
    assert get_user_ratings('Will') == [[42,3]]
