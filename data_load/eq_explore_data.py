#json 数据的处理
import json
import plotly.express as px
import pandas as pd
#json格式文件访问
filename = 'earthquake_data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #将数据转为python能处理的形式
#with open("earthquake_data/readable_file",'w') as f:
#    json.dump(all_eq_data,f,indent=4) #接受一个json格式数据写入到文件中 indent表示缩进设置

#提取地震信息
all_eq_dicts = all_eq_data["features"]
#print(len(all_eq_dicts))

#提取地震级别
mags = []
"""
for eq_dict in all_eq_dicts:
    msg = eq_dict['properties']['mag']
    mags.append(msg)
#print(mags)
"""
#提取位置数据 通过经纬度取位置
titles = []
lons = []
lats = []
for eq_dict in all_eq_dicts:
    msg = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(msg)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
#绘制散点图
"""
#plotly的express 语法与matplotlib的语法类似
fig = px.scatter(
    x=lons,
    y=lats,
    labels={'x':'经度','y':'纬度'},
    range_x=[-200,200], #范围
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
)
fig.write_html('global_eq.html') # 保存到文件
fig.show()
"""
#另一种定义图表方式，使用pandas 定义一个数据封装，方便数据处理
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200], #范围
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10, #将显示尺寸缩放到10
    color='震级', # 按照震级显示不同颜色 范围从蓝色到红色再到黄色， 数值越小越蓝
    hover_name='位置'
)
fig.write_html('global_eq.html') # 保存到文件
fig.show()