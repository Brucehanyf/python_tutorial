# 模拟掷骰子
from data_visualization.day02.die import Die
import pygal

# 创建一个D6
die_1 = Die()


# 储存掷骰子的结果
result = []
for roll_number in range(1000):
    result.append(die_1.roll())
print(result)

# 分析结果
frequencies = []
for value in range(1, die_1.num_sides+1):
    frequency = result.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对数据进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist._y_title = "Frenquency of Result"

hist.add(title='D6',values=frequencies)
hist.render_to_file('die_visual.svg')
