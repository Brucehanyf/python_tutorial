# csv分析Csv
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。

# file_name = 'sitka_weather_07-2014.csv'
file_name = 'death_valley_2014.csv'
with open(file_name) as file_object:
    reader = csv.reader(file_object)
    # 调用next()一次，读取当前第一行文件
    header_row = next(reader)
    print(header_row)

    # 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    dates,hights,lows = [],[],[]
    for row in reader:
        try:
            hight = int(row[1])
            curent_date = datetime.strptime(row[0],"%Y-%m-%d")
            low = int(row[3])
        except ValueError:
            print(curent_date,'missing data')
        else:
            hights.append(hight)
            dates.append(curent_date)
            lows.append(low)
    print(hights)

fig = plt.figure(figsize=(10,6))
# 设置透明度 alpha 0.5
plt.plot(dates,hights,c='red', alpha=0.5)
plt.plot(dates,lows,c='blue', alpha=0.5)
# 设置两个y值填充 指定填充颜色 facecolor 黄色
plt.fill_between(dates,hights,lows,facecolor='purple',alpha=0.2)
# 设置样式
plt.title('Daily high temperatures, July 2014',fontsize= 14)
plt.xlabel('',fontsize=16)
# 斜的标签日期
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=5)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()