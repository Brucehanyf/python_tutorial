try:
    # python 2.X版本
    from urlib2 import urlopen
except ImportError:
    # python 3.x版本
    from urllib.request import urlopen
import json
import pygal
import math

# json_url = "https://github.com/Brucehanyf/config/blob/master/respo/btc_close_2017.json"
# json_url = "http://www.kuaidi100.com/query?type=yuantong&postid=11111111111"
# response = urlopen(json_url)
# # 读取数据
# req = response.read()
#
# # 将数据写入文件
# with open('btc_close_2017_urllib.json','wb') as file_object:
#     file_object.write(req)
#
# # 加载json格式s
# file_urllib = json.load(req,encoding='utf-8')
# print(file_urllib)

file_name = "btc_close_2017.json"
with open(file_name,encoding='utf-8') as file_object:
    btc_data = json.load(file_object)
# 打印每一天的信息
# for btc in btc_data:
#     date = btc['date']
#     month = int(btc['month'])
#     week = int(btc['week'])
#     weekday = btc['weekday']
#     # 将字符串转换成浮点数 在转换成整型
#     close = int(float(btc['close']))
#     print("{} is month {} week {} ,{}, the close price is {} RMB".format(date,month,week,weekday,close))

# 创建五个列表，分别存储日期和收盘价格
dates, months, weeks, weekdays, close = [], [], [], [], []
for btc in btc_data:
    dates.append(btc['date'])
    months.append(int(btc['month']))
    weeks.append(int(btc['week']))
    weekdays.append(btc['weekday'])
    # 将字符串转换成浮点数 在转换成整型
    close.append(int(float(btc['close'])))
# x_label_rotation X轴顺时针旋转20度  show_minor_x_labels 是不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation = 20, show_minor_x_labels=False)
line_chart.title = "收盘价（￥）"
line_chart.x_labels = dates
N= 20 # X轴坐标没隔20天显示一次
# 第一个冒号表示元素起始位置，第二个冒号表示元素的终止位置，第三个数（也就是N）表示步长，
# 在此例中，N = 20， 从dates[0]开始取，经过20个数再取，也就是dates[20]，直到列表末尾才结束
# line_chart.x_labels_major = dates[::N] 注意此处的参数
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图.svg')

# 时间序列特征初探
#收盘价对数变换折线图
close_log = [math.log10(a) for a in close ]
line_chart.title = "收盘价对数变换"
line_chart.add('收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x,sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month],'收盘价日均值','日均值')
line_chart_month

# 收盘价周日均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],close[1:idx_week],'收盘价周日均值','周日均值')
line_chart_week

# 收盘价均值
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) +1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week],'收盘价星期均值','星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file("收盘价星期均值.svg")

# 收盘价数据仪表盘
with open('收盘价Dashboard.html','w',encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in['收盘价折线图.svg','收盘价对数变换折线图.svg','收盘价日均值.svg',
        '收盘价周日均值.svg','收盘价星期均值.svg']:
        html_file.write(' <object type = "image/svg+xml" data={0} height=500></object>\n'.format(svg))
    html_file.write('</body></html>')




