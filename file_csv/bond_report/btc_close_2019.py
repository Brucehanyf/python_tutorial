try:
    # python 2.X版本
    from urlib2 import urlopen
except ImportError:
    # python 3.x版本
    from urllib.request import urlopen
import json
import pygal
import math

file_name = "btc_close_2017.json"
with open(file_name,encoding='utf-8') as file_object:
    btc_data = json.load(file_object)
# 打印每一天的信息
# 创建五个列表，分别存储日期和收盘价格
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc in btc_data:
    dates.append(btc['date'])
    months.append(int(btc['month']))
    weeks.append(int(btc['week']))
    weekdays.append(btc['weekday'])
    # 将字符串转换成浮点数 在转换成整型
    close.append(int(float(btc['close'])))

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    zip_param = zip(x_data,y_data)
    # print(list(zip_param))
    "[(1, 6928), (1, 7070), (1, 7175), (1, 7835), (1, 6928), (1, 6196), (1, 6262)..."
    sort_zip = sorted(zip_param)
    print(list(sort_zip))
    "[(1, 5383), (1, 5566), (1, 5648), (1, 5674), (1, 5700), (1, 5730), "
    print("11111")

    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x,sum(y_list) / len(y_list)])
    x_unique, y_mean = zip(*xy_map)
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month],'收盘价日均值','日均值')
print(line_chart_month)



