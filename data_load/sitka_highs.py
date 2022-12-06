import csv
import matplotlib.pyplot as plt
from datetime import datetime
# 读物csv文件内容
#filename = 'sitka_weather_07-2018_simple.csv'
filename = 'sitka_weather_2018_simple.csv' # 整年数据
with open(filename) as f:
    reader = csv.reader(f)   #返回一个阅读器对象
    header_row = next(reader)
   # print(header_row)   #next只调用一次，显示文件第一行

    #enumerate显示索引号打印
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    #从文件中获取最好温度
    highs = []
    dates = []
    lows = []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')  # 获取日志
        try:
            high = row[5]
            low = row[6]  # 最低温度
        except ValueError:
            print(f"missing data for {date}")
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)
# 根据最高温度绘制图表
#plt.style.use('seaborn')
fig,ax = plt.subplots(figsize=(10,5),dpi=128)
ax.plot(dates,highs,c='red',alpha=0.5) # alpha 表示透明度 0 表示完全透明
ax.plot(dates,lows,c='blue',alpha=0.5)
# 表区域着色 向fill_between传递一个x，两个y， 将之间着色
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置图片格式
ax.set_title('2018年最高温度',fontproperties='simhei',fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate() #绘制斜体的日期标签
ax.set_ylabel('温度（F）',fontproperties='simhei',fontsize=14)
ax.tick_params(axis='both',which='major',labelsize=14)
plt.show()
