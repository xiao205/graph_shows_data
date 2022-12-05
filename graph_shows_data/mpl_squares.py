import matplotlib.pyplot as plt
from matplotlib import rcParams
#pyplot 包含了很多用于生成图表的函数
# 绘制简单的折线图

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]
#这个函数可以在一个图片中绘制一个或多个图表1
plt.style.use('seaborn')  #图片内饰
fig,ax = plt.subplots()
#fig 表示整张图片 ， ax 表示图片中的各图表
ax.plot(input_values,squares,linewidth=3) #根据指定的数据绘制图表  线条粗度3
# 在途中添加字体
ax.set_title("平方数",fontproperties='simhei',fontsize=24)
ax.set_xlabel("值",fontproperties='simhei',fontsize=14)
ax.set_ylabel("值得平方",fontproperties='simhei',fontsize=14)
#可量度值的大小
ax.tick_params(axis='both',labelsize=14)

plt.show()  # 展示
