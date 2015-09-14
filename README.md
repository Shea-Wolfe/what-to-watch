# Getting Started
For any of this to run make sure you download the movielens 100k zip from http://grouplens.org/datasets/movielens/ and unpack it in the directory with these files.

In addition due to the interface importing for the core libraries make sure that movie_lib.py is in the same directory before you run interface_movie_lib.py or else it will not run.

To run interface_movie_lib.py on the command line enter $ python interface_movie_lib.  

To run test_movie_lib.py make sure you have nose initialized and then on the command line enter $ nosetests

movie_lib.py is a file that holds classes, methods, and functions for use in interface_movie_lib.py and should not be run.  Feel free to open it with your editor of choice to see what it's doing.

## Description
movie_lib.py creates instances of all the data from the MovieLens 100k for three classes, Movie, User, and Rating.  

It also populates a dictionary of all users and all movies where the key is the user or movie id and the value is the instance of User or Movie at that key.

There are three functions (get_items, get_users, and get_data) which actually imports the relevant data from the MovieLens files.

get_top_x returns a sorted list of movies based on their average review score.  it requires no arguements but returns the top 50 by default and can take different numbers.

Euclidean distance formula was copied from James Allen and returns the distance between two lists (for instance user ratings).

get_user_suggest just returns one of the top 5 movies (at random) that the user hasn't seen yet (as defined by average reviews for movies with at least 10 reviews)

compare_users looks at the overlapping movies that two users have seen and sees how similar their reviews were on each returning an Euclidean distance score.

get_unshared_movies takes a primary user and a secondary user and returns a tuple of a dictionary of movies that only the secondary user has seen as well as the secondary user id.

find_similar_user uses compare_users to build a list of users within a certain Euclidean distance of the primary user (set to .20).  

Get user fav movie also takes the results from find similar user but returns one of the top 5 titles based on that users reviews ONLY.

similar_user_pick brings all the above functions together to have each similar user pick a movie they enjoyed (in their top 5) that the user hasn't seen.  Then the average rating for that movie is multiplied by their Euclidean distance and the picked movie that ends with the highest score is recommended to the user.  This way the overall scores for the movie matter some but so does how similar the two users are.

The functions in interface_movie_lib are mostly getting and checking user input or quickly printing strings for formatting purposes.
