import matplotlib.pyplot as plt
# 绘制散点图
# 图片内饰
plt.style.use("seaborn")
#x_values = [1,2,3,4,5]
#y_values = [1,4,9,16,25]

#进行自动计算取值
x_values = range(1,10)
y_values = [x ** 2 for x in x_values]
fig,ax = plt.subplots()
#ax.scatter(x_values,y_values,c='red',s=10) # 准备一个点
#随着y的值，颜色变化有浅到深
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=100) # 准备一个点

#标题
ax.set_title("平方数",fontproperties='simhei',fontsize=24)
ax.set_xlabel("值",fontproperties='simhei',fontsize=14)
ax.set_ylabel("值得平方",fontproperties='simhei',fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)

plt.show() #展示图表
#保持图片在指定目录下，bbox_inches 是指删除图片其余空白地方
#plt.savefig('f2.png',bbox_inches='tight')