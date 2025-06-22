"""
JSON 和PYTHON 的转化
创建折线图
"""
# import json
#
# data = [{"name":"蔡徐坤","age":18},{"name":"lxn","age":20}]
#
# json_str = json.dumps(data,ensure_ascii=False)
#
# print(type(json_str))
# print(json_str)
#
# d = {'name':"序号龙","段位":'s6第一个王者'}
# D = json.dumps(d,ensure_ascii=False)
# print(D)
#
# S = '[{"name": "蔡徐坤", "age": 18}, {"name": "lxn", "age": 20}]'
# s = json.loads(S)
# print(type(s))
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts,VisualMapOpts
#
# line = Line()
# line.add_xaxis(["2027","2028","2029"])
# line.add_yaxis('工资(k)',[30,40,50])
# line.set_global_opts(
#     title_opts=TitleOpts(title="以后lxn的毕业薪资",pos_left='center',pos_bottom="0"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
# line.render()

from pyecharts.charts import  Map
from pyecharts.options import  VisualMapOpts

map = Map()
data = [
    ("北京市",8000),
    ("上海市",6000),
    ("广东省",30000),
    ("湖北省",1001),
    ("浙江省",10000),
    ("江苏省",3000),
    ("福建省",2000),
    ("云南省",2000),
    ("山东省",1500)
]
map.add("lol奎桑提玩家分布图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':1000,'label':'1-99','color':'#CCFFFF'},
            {'min':1000,'max':2500,'label':'99-199','color':'#FFFF99'},
            {'min':2500,'max':3500,'label':'199-299','color':'#FF9966'},
            {'min':3500,'max':7000,'label':'299-399','color':'#FF6666'},
            {'min':7000,'max':9000,'label':'399-499','color':'#CC3333'},
            {'min':9000,'max':12000,'label':'499-599','color':'#990033'},
            {'min':12000,'max':40000,'label':'599-699','color':'#000000'}
        ]
    )
)



map.render()
























































































































































































