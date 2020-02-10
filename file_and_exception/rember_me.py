# 重构演示
import json


def greet_user():
    '''问候用户'''
    username = get_stored_username()
    if username:
        print('Welcome back '+username)
    else:
        username = get_new_username()
        print('we will remember you when you come back'+username)


def get_stored_username():
    '''获取已经存储的用户'''
    filename = "username.json"
    try:
        with open(filename) as file_reader:
            username = json.load(file_reader)
            print('username is ' + username)
            return username
    except FileNotFoundError:
        return None


def get_new_username():
    '''提示用户输入用户名'''
    username = input('please enter a new username')
    filename = 'username.json'
    with open(filename, 'w') as file_writer:
        json.dump(username, file_writer)
        print('username'+ username +'have stored')
    return username


greet_user()
