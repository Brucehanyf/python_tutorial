# 绘制简单的折线图
import matplotlib.pyplot as plt

input_value =[1,2,3,4,5]
squares = [1,4,9,16,25]
# 指定线条宽度 linewidth = 5
# 指定输入值
plt.plot(input_value, squares, linewidth = 5)


# 设置图标标题、坐标轴加上标签
plt.title("Square Number",fontSize = 24)
plt.xlabel("Value",fontSize = 24)
plt.ylabel("Square of value", fontSize=24)

# 设置刻度标记的大小  lablesize不存在
plt.tick_params(axis='both',size = 1)

plt.show()



