from movie_lib import *

def main():
    print('Loading data.  Please hold.')
    get_items()
    get_users()
    get_data()
    current_user = get_user_id()
    print(current_user)

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

if __name__ == '__main__':
    main()
