# 列表

bicycles = ['trek','cann','redline','special']
print(bicycles)

# 访问数组元素
print(bicycles[0])
# 访问最后一个个元素
print(bicycles[-1])

# 修改列表的元素
bicycles[0] = "bruce"
print(bicycles)

# 在列表中添加元素
bicycles.append('bbb')
print(bicycles)

# 指定位置添加元素
bicycles.insert(0,'aaa')
print(bicycles)

# 从列表中删除元素 IndexError: list assignment index out of range
del bicycles[0]
print(bicycles)

# 使用pop()删除元素
last_one = bicycles.pop()
print(last_one)
print(bicycles)

# 弹出任意位置的元素
last_two = bicycles.pop(2);
print(last_two)
print(bicycles)

# 根据值删除列表中的元素 只删除第一个指定的值
bicycles.remove('bruce')
print(bicycles)

# 使用sort() 对列表进行永久排序
cars = ['x','z','a','c','t']
# cars.sort()
# 降序排列
# cars.sort(reverse=True)
# print(cars)

# 使用sorted() 临时排序 可以传参reverse=True
print(sorted(cars))
print(cars)

# 反转数组
cars.reverse()
print(cars)

# 确定数组的长度
length = len(cars)
print(length)

# 数组下表越界
mobiles = []
print(mobiles[-1])













