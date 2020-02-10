# 函数
def greet_user():
    print ('hello world!')
greet_user()

def greet_user(userName):
    print ('hello '+userName+'!')
greet_user('bruce')

# 关键字实参 默认值得形参要放在后边
def describe_pet( pet_name, animal_type ='Dog'):
    print('i have a '+animal_type)
    print ('my '+animal_type+"'s name is "+pet_name)
describe_pet(animal_type='Dog',pet_name='TT')
describe_pet(pet_name='TT')

# 返回值
def get_full_name(first_name, last_name):
    full_name = first_name +' '+ last_name
    return full_name.title()
full_name = get_full_name('Bruce','Han')
print (full_name)

def get_full_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = full_name = first_name +' '+middle_name+' '+ last_name
    else:
        full_name = full_name = first_name + ' ' + last_name
    return full_name.title()
full_name = get_full_name('Bruce','Han','M')
print (full_name)

# 返回字典
def build_person(first_name, last_name):
    person = {'first_name':first_name,'last_name':last_name}
    return person
print (build_person('bruce','han'))

# 传递列表
def greet_users(names):
    for name in names:
        print ('hello '+ name)

greet_users(['alice','bob','cherry'])

def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print ('Print model .....'+current_design)
        completed_models.append(current_design)
def show_completed_model(completed_models):
    print('The following is completed model:')
    for model in completed_models:
        print(model)

# 拆分处理函数
unprinted_models = ['AAA','BBB','CCC','DDD']
completed_models = []
# 不保存原来的数据
# print_model(unprinted_models,completed_models)
## 保存原来的记录 需要创建副本
print_model(unprinted_models[:],completed_models)
show_completed_model(completed_models)
print ('原来的表格数据'+str(unprinted_models))

# 传递任意数量的参数
def make_pizza(*toppings):
    print (toppings)
make_pizza('apple','banana','orange','potato')

# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    print ('make a ' + str(size) + ' pizza fowing toppings:')
    for topping in toppings:
        print (topping)
make_pizza(10,'apple','banna','orange')

# 使用任意数量的关键字实参 ** 创建字典类型参数
def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
info = build_profile('FI','albert',location = 'SZ',field = 'physics')
print (info)

# 将函数存贮在模块中
import base.pizza
base.pizza.pizza_factory(16,'sugger')

# 导入特定函数 模块名 函数名 多个函数名可以用逗号隔开
from base.pizza import pizza_factory
pizza_factory(20,'sugger','coffee')

# 使用AS给函数指定别名
from base.pizza import pizza_factory as mp
mp(200,'vegetables')

# 使用as 给指定模块指定别名
import base.pizza as p
p.pizza_factory(1212,'app','tomato')

# 导入模块的所有函数
from base.pizza import *

# 函数编写指南
# 给形参默认值时,等号两边不要有空格 电泳关键字也不要有参数
# def function_name(parameter_0,parameter_1='default_value')

# 导入包要包含包的名字







