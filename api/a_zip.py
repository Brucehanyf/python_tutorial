# zip函数
# zip() 函数用于将可迭代的对象作为参数，
# 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，
# 这样做的好处是节约了不少的内存。
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,9]
zipped = zip(c,a)
# print(list(zipped))
# 之后取出最小集配对

# 解压
# a1, a2 = zip(*zip(a,b))
a1, a2 = zip(*zipped)
print(a1)
print(a2)

from itertools import groupby
# 测试无用变量 y_list = [v for _, v in y]
map = []
for x,y in groupby(sorted(zip(c,a),key=lambda _:_[0])):
    list = [v for _,v in y]
    print(x,list)
    map.append([x,sum(list)/len(list)])
z1, z2 = zip(*map)
print(z1, z2)