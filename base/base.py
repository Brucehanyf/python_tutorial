# Python3 支持的六大基本数据类型
# Numbers（数字）
# String（字符串）
# Tuple（元组）
# List（列表）
# Dictionary（字典）

print('----- number action -----')
# 一：Numbers
# Python支持四种不同的数字类型：
# int（整数类型）
# float (浮点类型)
# complex（复数）
# bool （布尔值）

n_int = 1
n_complex = 9.322e-36j
n_dounle = 1000.0
n_bool = True

# type() 函数判断
print(type(n_bool))

# 用 isinstance来判断类型
print(isinstance(n_int, int))

# isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# del语句删除对象引用 del var1[,var2[,var3[....,varN]]]] = 1
del n_int,n_complex

# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
print(5/2)
print(5//2)
print('----- number action -----')

print('----- str action -----')
# 二、字符串
str1 = 'brucehan'
print(str1[2:5])  # 截取第三个和第六个
print(str1[-2:]) # 截取倒数第二个到最后的
print(str1[:])
print(str1[0:-1]) # 截取第一个到倒数第一个
print(str1 * 2) # 输出字符串两次

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，
# 可以在字符串前面添加一个 r，表示原始字符串：

print('Bruce\'s name')
print('Bruce\nAlice')
print(r'Bruce\nAlice')

# Python中的字符串不能改变
word = 'Python'
# word[1] = 'N' # 'str' object does not support item assignment
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))


# 三引号保持字符串原样输出
# errHTML = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''

# cursor.execute('''
# CREATE TABLE users (
# login VARCHAR(8),
# uid INTEGER,
# prid INTEGER)
# ''')

print('----- str action -----')

print('----- list action -----')
# 三、列表List
# 列表中的元素类型可以不同
# 列表支持索引取值 变量[头下标:尾下标]
# 列表可以嵌套
# 列表可以修改其中的元素
list_1 = ['abc', 123, 2.33, 2.e-36j]
tinylist = ['bec',456]
print(list_1[0])
print(list_1[2:4])
print(list_1[:])
print(list_1 * 3) # 输出两次
print(list_1 + tinylist) # 连接列表
list_1[0] = 'python' # 修改某个坐标的值
print(list_1)

letter = ['a','b','c','d','e','f','g','h','j','k']
# 从 0-9 间隔三个位置输出字符串
print(letter[0:9:3])
# -1 从最后一个 到最后边 -1 逆向
print(letter[-1::-1]) # 逆向输出

# 删除列表元素
del letter[0]
print(letter)

# 将元组转换成数组
tuple_list = ('ab','cd','ef','fg','sf')
list_tuple = list(tuple_list)

# list长度
len(list_tuple)
# List APi
# 1	list.append(obj) # 在列表末尾添加新的对象
# 2	list.count(obj) # 统计某个元素在列表中出现的次数
# 3	list.extend(seq) # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj) # 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj) # 将对象插入列表
# 6	list.pop([index=-1]) # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj) # 移除列表中某个值的第一个匹配项
# 8	list.reverse() # 反向列表中元素
# 9	list.sort( key=None, reverse=False) # 对原列表进行排序
# 10	list.clear() # 清空列表
# 11	list.copy() # 复制列表


print('----- list action -----')

print('----- tuple action -----')
# 四 Tuple（元组）
# 元组和列表类似 元组不能修改，写在括号里面用逗号分隔
# 可以把字符串看成一个特殊的元组
tuple1 = ('ab','cd','ef','fg','sf')
tiny_tuple = ('12','34','56')
print(tuple1[1])
print(tuple1[1:3])
print(tiny_tuple * 2)
print(tuple1 + tiny_tuple)
# 元组内的list是可以修改的
list1 = [1,2,3,4,5,6,7]
list2 = [11,22,33,44,55,66,77]
list_tuple = (list, list1, list2)
list_tuple[1][0] = 110
print(list_tuple)

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tuple_one = (1,)

# 将list 转为元组
iterable = [1,2,3,4,5]
list_itera =  tuple(iterable)
print(list_itera)
# 删除整个元组
del tuple_one

# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
tup = ('r', 'u', 'n', 'o', 'o', 'b')
id1 = id(tup)
tup = (1,2,3) # 重新创建一个的地址引用
id2 = id(tup)
print(id1 == id2)

print('----- tuple action -----')
print('----- set  -----')
# Set（集合）
# 创建方法 用{value1，value2, value3} set（value）
# 空集合只能用set(list) 设置
set_1 = {'Abam',1,'dsfdsf','a','a'}
print(set_1)
print(set_1.__contains__('a'))
if 'a' in set_1:
    print('a is in the set')

a_list =['a','b','c']
a = set(a_list)
b = {'a','b','d'}
print('----- set action -----')
print(a-b) # a 和 b 的差集 a里面有b里面没有的
print(a | b) # a b的并集
print(a & b)  # a b的交集
print(a ^ b) # a b中同时不存在的值
print('----- set action -----')

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
# 移除元素 没有会报错
thisset.remove("Facebook")
thisset.discard("Facebook")
# 随机删除一个源元素
thisset.pop()
# 清空集合
thisset.clear()

print('----- set  -----')

# 五、字典 Dictionary(字典)
print('----- Dictionary action -----')
dict = {}
dict['1'] = 101
dict['2'] = 102
dict['3'] = 103
print(dict['1'])
print(dict.keys())
print(dict.values())
# 字典遍历
for k,v in dict.items():
    print(str(k) + "-" + str(v))
print('----- Dictionary action -----')

# 删除字典
# del dict['Name'] # 删除键 'Name'
# dict.clear()     # 清空字典
# del dict         # 删除字典


def a():
    '''这是文档字符串'''
    pass
print(a.__doc__)

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个，
# == 用于判断引用变量的值是否相等。
a_is = [1,2,3,4,5]
b_is = a_is[:]
print(a_is is b_is)
print(a_is == b_is)






















