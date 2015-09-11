from movie_lib import *
will = User(1)
steve = User(2)
movie1 = Movie(15, 'The Matrix')
movie2 = Movie(20, 'Brick')


def test_user_creation():
    assert will.id == 1
    assert steve.id == 2
    assert will.id != steve.id

def test_movie_creation():
    assert movie1.id == 15 and movie1.title == 'The Matrix'
    assert movie2.id == 20 and movie2.title == 'Brick'
    assert movie1.id != movie2.id


# def test_get_rating():
#     #Should return a list of Rating objects
#     assert movie.get_rating() == [3]
#
# def test_get_average_rating():
#     assert movie.get_average_rating() == 3
#
# def test_get_movie_title():
#     assert movie.get_movie_title() == 'Star Wars'
#
# def test_get_user_ratings():
#     assert will.get_user_ratings() == [[42,3]]
