# json dump存储
import json
# numbers = [1,3,5,7,8,10]
# file = 'number.json'
# with open(file,'w') as json_object:
#     json.dump(numbers,json_object)

# json导出
# file = 'number.json'
# with open(file) as json_object:
#     nums = json.load(json_object)
# print(nums)

# 记录用户名字
# username = input('please tell me your name')
# with open('username.json','w') as file_object:
#     json.dump(username,file_object)
# with open('username.json') as file_reader:
#     name = json.load(file_reader)
# print('your username is '+name+'!')

# 如果用户以前存储了用户名就直接读出来 没有则新建
username_file = 'username.json'
try:
    with open(username_file) as user_file_read:
        name = json.load(user_file_read)
        print('the user have exited the name is '+name)
except FileNotFoundError:
    username = input('please tell us your username!')
    with open(username_file,'w') as user_file_write:
        json.dump(username,user_file_write)
        print('we will remember your username '+ username +'when you come back')