# 绘制散列点图并设置其样式
import matplotlib.pyplot as plt

# s 设置散列表的大小
# plt.scatter(2,4, s=200)
# x_value = [1,2,3,4,5]
# y_value = [1,4,9,16,25]

x_value = list(range(1,1001))
y_value = [x**2 for x in  x_value]
# edgecolors 删除数据点的轮廓
# c color ='red' 指定红色 默认蓝色点黑色轮库 TODO 旧版本不兼容
# 使用自定义颜色
# plt.scatter(x_value, y_value, c =(0,0,8), edgecolors='none', s = 10)
# 使用颜色映射 cmap=plt.cm.Blues 蓝色渐变
plt.scatter(x_value, y_value, c =y_value, cmap=plt.cm.Blues, edgecolors='none', s = 10)
# plt.scatter(x_value, y_value, c ='red', edgecolors='none', s = 10)

# 设置标题
plt.title("Scatter Squares",fontsize = 14)
# 设置x轴y轴标签
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of value", fontSize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

# 自动保存图表
# bbox_inches='tight' 将多余空白剪裁掉
plt.savefig('squares_plot.png',bbox_inches='tight')

plt.show()