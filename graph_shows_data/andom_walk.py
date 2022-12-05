#随机漫步是这样行走得到的路径，每次行走都是完全随机的，没有明确的方向，结果是一系列随机决策决定的
from random import choice
import matplotlib.pyplot as plt
class Randomwalk:
    def __init__(self,num_points=5000):
        self.num_points = num_points

        #所有随机漫步的始于位子
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        #来生产漫步包含的点并决定每次漫步的方向
        #这里不断漫步直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            #选着前进的方向1 为右 -1 为左
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4]) #移动距离
            x_step = x_direction * x_distance # 下一步
            # 选着方向上下
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_distance * y_direction

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下一个点的x，y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
#绘制随机漫步图
while True:
    rw = Randomwalk()
    rw.fill_walk()
    print(rw.x_values)
    print(rw.y_values)
    plt.style.use("classic") #图片内饰
    #figsize 图形大小 dpi 表示分辨率
    fig,ax = plt.subplots(figsize=(10,6),dpi=128)
    point_numbers = range(rw.num_points)
    # cmap=plt.cm.Blues 点设定颜色，从浅蓝到深蓝
    #edgecolors = 'none' 删除每个点的周围的轮廓
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors = 'none',s=1) # 绘制图片
    #突出起点与终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    # plt.savefig('f2.png',bbox_inches='tight') #保持图片
    keep_running = input("make another walk?(y/n):")  # 进行多次的漫步图表
    if keep_running == 'n':
        break

