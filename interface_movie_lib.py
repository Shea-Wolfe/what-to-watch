from movie_lib import *

def main():
    print('Loading data.  Please hold.')
    get_items()
    get_users()
    get_data()
    current_user = get_user_id()
    print('\nWelcome user {}.'.format(current_user))
    while True:
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            number_of_movies()
        elif menu_choice == 2:
            print('{0}{1}{0}'.format(add_line(),get_user_suggest(current_user)))
        elif menu_choice == 3:
            print('{0}{1}{0}'.format(add_line(),get_popular_movie(find_similar_user(current_user))))
        elif menu_choice == 4:
            print('{0}{1}{0}'.format(add_line(),get_user_fav_movie(find_similar_user(current_user))))
        elif menu_choice == 5:
            list_all_movies()
        elif menu_choice == 6:
            add_review(current_user)
        elif menu_choice == 7:
            print('{0}{1}{0}'.format(add_line(),all_users[current_user].ratings))
        elif menu_choice == 8:
            break

def get_user_id():
    current_user = input('Please enter your user ID number! 1-943 > ').lower()
    if current_user == 'jean valjean':
        print('You are prisioner 24601!')
        current_user = '24601'
    elif current_user == 'who is number 1?':
        print('You are, number 6')
        current_user = choice([1,6])
    try:
        current_user = int(current_user)
    except:
        print('That is not a valid user id.  Please try again.')
        return get_user_id()
    if current_user > 943 and current_user != 24601 or current_user < 0:
        print('That is not a valid User Id.  Try again')
        return get_user_id()
    return current_user

def get_menu_choice():
    menu_choice = input('''\nPlease select your option from those below
    [1] Get a listing of top movies.
    [2] Get a movie recomendation.
    [3] Get a popular recomendation from a similar user.
    [4] Get a recomendation based on a similar user\'s favorites.
    [5] View all the movies in the database.
    [6] Add a new review.
    [7] View your existing reviews.
    [8] Exit the program.\n > ''')
    try:
        menu_choice = int(menu_choice)
    except:
        print('That is not number. Try again!')
        return get_menu_choice()
    if menu_choice > 8 or menu_choice < 1:
        print('That is not one of the options.  Try again!')
        return get_menu_choice()
    return menu_choice

def number_of_movies(all_movies=all_movies):
    movie_num = input('Please enter how many of the top movies you want to view. 1-100\n> ')
    try:
        movie_num = int(movie_num)
    except:
        print('Sorry I did not get that.  Please enter a number')
    if movie_num < 1:
        print('A number that exists please!')
        return number_of_movies()
    elif movie_num > 100:
        print('That is gonna get real messy real quick, perhaps a few less')
        return number_of_movies()
    movie_dict = get_top_x(movie_num)
    for item in movie_dict:
        print(all_movies[item[0]].title)

def list_all_movies(all_movies=all_movies):
    for movie in all_movies:
        print(movie, all_movies[movie].title)

def add_review(current_user):
    movie = input('''Please enter the ID of the movie you want to review.
    enter [movies] for a list of all movie IDs with titles.
    > ''')
    if movie == 'movies' or movie == 'm':
        list_all_movies()
    else:
        try:
            movie = int(movie)
        except:
            add_review(current_user)
        if movie < 0 or movie > 1682:
            print('Sorry, I do not have that movie in my database.\n Try again.')
            return add_review(current_user)
        else:
            print('Great, you have decided to review {}'.format(all_movies[movie].title))
            while True:
                try:
                    score = int(input('Please enter your review score from 1 to 5 with 1 being the lowest.\nWhole numbers only please.\n> '))
                except:
                    print('That is not a valid score. Try again.')
                    continue
                if score > 0 and score < 6:
                    print('Review added.  You gave {} a {} out of 5'.format(all_movies[movie].title,score))
                    Rating(current_user, movie, score)
                    break
                elif score < 0 or score > 5:
                    print('Please enter a score from 1 to 5.')

def add_line():
    return '\n----------------------------------------\n'

if __name__ == '__main__':
    main()
