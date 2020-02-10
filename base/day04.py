# if 语句
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bmw'
print (car == 'bmw')

if car != 'bmww':
    print (car.lower())

# 检查多个条件
age_0 = 22
age_1 = 18
print (age_0 >=21 and age_1 >=21)

# 使用or检查多个条件
print(age_0 >= 21 or age_1 >= 21)

# 检查特定值是否包含在列表中
topics = ['mushroom','onion','pineapple']
print ('mushroom' in topics)

# 检查特定值不包含在列表中
print('mm' not in topics)

# 布尔表达式
game_active = True
can_edit = False

# if else 语句
age = 1
if age > 18:
    print ('adult')
else:
    print ('children')
# if elseif elseif else 语句
if age >= 1:
    print ('age 一岁')
elif age < 18:
    print ('age 介于 1-18')
else:
    print ('age is adult')

# 检查列表是否为空
list = []
if list:
    print ('不是空的')
else:
    print ('空的')












    


