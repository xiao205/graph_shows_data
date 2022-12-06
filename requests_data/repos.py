import requests
from plotly.graph_objs import Bar
from plotly import offline
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#github api 版本
headers={'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)  #获取web数据
# 打印响应码
print(f"status code: {r.status_code}")
response_dict = r.json()# 将信息转为python的字典格式 ，之后就可是处理数据了

# 处理结果
#print(response_dict.keys())
print(f"total repositories:{response_dict['total_count']}")  #总存储仓库数
#有关仓库信息
repo_dicts = response_dict['items']
#print(f'repositories returned: {len(repo_dicts)}')

#取到第一个仓库
#repo_dict = repo_dicts[0]
#for key in sorted(repo_dict.keys()):
#    print(key)
"""
for repo_dict in repo_dicts:
    #打印仓库的一些相关信息
    print(f"name: {repo_dict['name']}")
    print(f"owner: {repo_dict['owner']['login']}")
    print(f"stars: {repo_dict['stargazers_count']}")
    print(f"url: {repo_dict['html_url']}")
    print(f"created: {repo_dict['created_at']}")
    print(f"updated: {repo_dict['updated_at']}")
    print(f"description: {repo_dict['description']}")
"""
# 绘制直方图
repo_names = []
starts = []
labels = []
repo_links = []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_names.append(repo_name)
    starts.append(repo_dict['stargazers_count'])
    # 一些提示信息
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)
    # 添加ur连接
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  #添加一个a标签
    repo_links.append(repo_link)
#可视化数据
data = [
    {
        'type':'bar',
        'x':repo_links,  #x轴仓库名+一个a标签连接url
        'y':starts,
        'hovertext':labels,
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
    'title':'最受欢迎的python项目',
    'titlefont':{'size':28}, # 表名字号
    #轴的标签字号和刻度的标签字号设置
    'xaxis':{'title':'repository','titlefont':{'size':24},'tickfont':{'size':14}},
    'yaxis':{'title':'starts','titlefont':{'size':24},'tickfont':{'size':14}},
}
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')