# 随机漫步显示类
import matplotlib.pyplot as plt
from data_visualization.day01.random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

# 设置窗口尺寸
plt.figure(dpi=128,figsize=(10,6))
# 随机显示
# plt.scatter(rw.x_values,rw.y_values, s = 15)

# 设置随机漫步图的样式 先后着色，去边缘
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values, c= point_numbers, cmap=plt.cm.Blues, edgecolors= 'none', s = 1)

# 重新绘制起点和终点 直径S 100
plt.scatter(0, 0, c='yellow',edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none',s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
