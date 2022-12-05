# 将对掷筛子的结果进行图片分析
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline
class Die:
    # 表示一个骰子的类
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides
    def roll(self):
        return  randint(1,self.num_sides) #返回1-6点随机一个

die = Die() #创建一个骰子
die2 = Die() # 同时玩两个骰子
results = [] #几次的结果存储在一个列表中
#掷色子100次
for roll_num in range(100):
    result = die.roll() + die2.roll()
    results.append(result)

#分析结果
frequencies = [] # 用于存储每种点出现次数
max_result = die.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)  # 统计次数
    frequencies.append(frequency)
# 直方图显示
x_values = list(range(2,max_result+1)) # x轴
data = [Bar(x=x_values,y=frequencies)]  # Bar 用于绘制条形图的数据集
x_axis_config = {'title':'结果','dtick':1} #'dtick 显示每个刻度值
y_axis_config = {'title':'结果统计'}
# 指定图标布局
my_layout = Layout(title='掷一个色子的结果图',xaxis=x_axis_config,yaxis=y_axis_config)
#生成条形图
offline.plot({'data':data,'layout':my_layout},filename = 'd1.html')