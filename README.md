# Getting Started
For any of this to run make sure you download the movielens 100k zip from http://grouplens.org/datasets/movielens/ and unpack it in the directory with these files.

To run interface_movie_lib.py on the command line enter $ python interface_movie_lib.

To run test_movie_lib.py make sure you have nose initialized and then on the command line enter $ nosetests

movie_lib.py is a file that holds classes, methods, and functions for use in interface_movie_lib.py and should not be run.  Feel free to open it with your editor of choice to see what it's doing.

## Description
movie_lib.py creates instances of all the data from the MovieLens 100k for three classes, Movie, User, and Rating.  

It also populates a dictionary of all users and all movies where the key is the user or movie id and the value is the instance of User or Movie at that key.

There are three functions (get_items, get_users, and get_data) which actually imports the revelant data from the MovieLens files.

get_top_x returns a sorted list of movies based on their average review score.  it requires no arguements but returns the top 50 by default and can take different numbers.

Euclidean distance formula was copied from James Allen and returns the distance between two lists (for instance user ratings).

Compare Users takes two users and returns lists of the scores they gave to movies they both reviewed.

Get unshared movies returns a dictionary of movies that one user has seen that the other hasn't.

Find similar user currently looks at all users and returns the one with the closest euclidean distance from the current user.  It then creates a dictionary of movies that the other user has seen using get unshared movies

Get popular move takes the results from find similar user and returns one of the top 5 titles that the similar user has seen based on average ratings.

Get user fav movie also takes the results from find similar user but returns one of the top 5 titles based on that users reviews ONLY.

The functions in interface_movie_lib are mostly getting and checking user input or quickly printing strings for formatting purposes.
