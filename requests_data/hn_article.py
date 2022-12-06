# 回去hacker news 网站的api
"""
该网站右很多文章和评论信息，且获取不需要通过注册获取密钥
"""
import requests
import json
from plotly.graph_objs import Bar
from plotly import offline
"""
# 获取该网站的一个文章
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"status code: {r.status_code}")
response_dict = r.json()
readable_file = 'readable_hn_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict,f,indent=4)#接受一个json格式数据写入到文件中 indent表示缩进设置
"""
#获取网站排名前的文章ID
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# 处理每个文章信息
submission_ids = r.json()   #所有文章id
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对每一个文章 获取信息
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    response_dict = r.json() #将信息转为python的字典格式 ，之后就可是处理数据了
    # 将文章信息写到字典中
    """
    submission_dict = {
        'title':response_dict['title'],
        'hn_link':f"http://news.ycombinator,com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }
    """
    submission_dicts.append(response_dict)
#submission_dicts = sorted(submission_dicts,key=temgetter('comments'),reverse=True)# 排序

# 绘制直方图
titles = []
#hn_links = []
comments = []
ids = []
for submission_dict in submission_dicts:
    title = submission_dict['title']
    #url = submission_dict['url']
   # hn_link =  f"<a href='{url}'>{id}</a>"
    submission_id = submission_dict['id']
    comment = submission_dict['score']
    titles.append(title)
    #hn_links.append(hn_link)
    comments.append(comment)
    ids.append(submission_id)
print(comments)
print(ids)

#可视化数据
data = [
    {
        'type':'bar',
        'x':ids,  #x轴仓库名+一个a标签连接url
        'y':comments,
        'hovertext':titles,
        #对条形颜色布局设置
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{'width':1.5,'color':'rgb(25,25,25)'}
        },
        'opacity':0.6,   #条形的不透明设置
    }
]
#图片布局
my_layout = {
    'title':'最受欢迎的文章',
    'titlefont':{'size':28}, # 表名字号
    #轴的标签字号和刻度的标签字号设置
    'xaxis':{'title':'wenzhang','titlefont':{'size':24},'tickfont':{'size':14}},
    'yaxis':{'title':'haoping','titlefont':{'size':24},'tickfont':{'size':14}},
}
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_hnsubmission.html')
