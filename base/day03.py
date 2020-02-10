# 操作列表
# 遍历整个列表
magicians = ['alice','david','caro']
for magician in magicians:
    print(magician)
    print(magician.title())
print("-----------")

# 使用函数range() 含头不含尾
for val in range(1,5):
    print(val)

# 使用range() 创建数字列表
list1 = list(range(1,20))
print(list1)

# range() 指定步长
list2 = list(range(2,11,10))
print(list2)

# range() 创建任何数组
squares = []
for val in range(1,10):
 squ = val**2
 squares.append(squ)
print(squares)

# 对数字列表进行简单的运算
print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析 创建列表 val**2 表达式 for..用于表达式提供值 结尾没有冒号
squares2 = [val**2 for val in range(1,11)]
print(squares2)

# 使用列表中的一部分 第二-第四个元素
players = ['a','b','c','d','e','f']
print(players[1:4])
# 没有指定第一个索引则从头开始
print(players[:4])
# 没有指定最后一个索引则一直到最后
print(players[2:])

# 使用负数来返回距离列表末尾的距离
print(players[-2:])

# 遍历切片
for val in players[-2:]:
    print(val)
# 复制整个列表
food = ['apple','banana','orange']
my_food = food[:]
print(food)
print(my_food)

food.append('kfc')
my_food.append('chicken')
print(food)
print(my_food)

# food = my_food 则是指向同一地址

# 元组
# 定义元组 dimensions[0] = 5 元组不支持直接复制
dimensions = (3,5)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 不能修改元组的值，但是可以赋值
dimensions = (100,200)
print(dimensions)












