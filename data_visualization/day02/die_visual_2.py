# 同时掷两个骰子 总点数
# 模拟掷骰子
from data_visualization.day02.die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die(10)



# 储存掷骰子的结果
result = []
for roll_number in range(1000):
    result.append(die_1.roll() + die_2.roll())
print(result)

# 分析结果
frequencies = []
max_num = die_1.num_sides + die_2.num_sides
for value in range(2, max_num+1):
    frequency = result.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对数据进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling Two D6 1000 times.'
hist.x_labels = list(range(2,max_num+1))
hist.x_title = "Result"
hist._y_title = "Frenquency of Result "

hist.add(title='D6',values=frequencies)
hist.render_to_file('die_visual_2.svg')
