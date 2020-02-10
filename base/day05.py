# 字典 类似map的结构
#定义字典
alien_0 = {'color':'green','point':5}

# 访问字典中的值
print(alien_0['color'])
print(alien_0['point'])
new_point = alien_0['point']
print ('you just have '+ str(new_point) +'points')

#添加键值对
alien_0['x_position'] = 1
alien_0['y_positon'] = 10
print (alien_0)

# 创建一个空的字典
alien_1 = {}
alien_1['color'] = 'Blue'
alien_1['points'] = 109
print (alien_1)

# 修改字典中的值
alien_1['color'] = 'Red'
alien_1['points'] = 10
print (alien_1)

# 删除键值对
del alien_1['color']
print (alien_1)

favorite_language = {
    'jen':'python',
    'sarah':'c',
    'bob':'rubby',
    'phil': 'python'
}
print ("bob favorite language is "+ favorite_language['bob'])

# 遍历字典
user_0 = {
    'username':'User',
    'age':10,
    'gender':'girl'
}
# 遍历字典中的键值对
for key,val in user_0.items():
    print (str(key) + str(val))

# 遍历字典中的所有键
for key in user_0.keys():
    print (key)
# 隐式遍历所有键
for name in user_0:
    print (name)

# 按顺序遍历字典中的所有键

for name in sorted(user_0.keys()):
    print (name.title()+' thank you!')

# 遍历字典中的所有值
for value in user_0.values():
    print ('value:  '+str(value))

# 嵌套语句
alies_s = [alien_1,alien_0]
print (alies_s)

alies_s = []
for alien in range(30):
    new_alien = {'color':'red','point':alien,'speed':'slow'}
    alies_s.append(new_alien)
print (alies_s)

# 字典中存列表
pizz = {
    'crust':'thick',
    'toppings':['mushroom','extra_cheese']
}

favorite_languages ={
    'jen':['python','java'],
    'sarch':['c','c##'],
    'edward':['rubby','jumlia'],
    'bob':['js','go']
}
for name,languages in favorite_languages.items():
    for language in languages:
        print (language)
# 在字典中存储字典
users = {
    'alice': {
        'first':'alice',
        'last':'A',
        'location':'BJ'
    },
    'bruce': {
        'first':'bruce',
        'last':'B',
        'location':'SZ'
    },
    'Cherry': {
        'first':'cherry',
        'last':'C',
        'location':'GZ'
    }
}
for user,user_info in users.items():
    print ('user info: ' + user_info['first'] + user_info['last']+ user_info['location'])














