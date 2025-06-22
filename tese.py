"""
北京2020年7.2疫情积累确诊人数
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/python文本/china_provincedata.json",'r',encoding="UTF-8")
data = f.read()#所有省份具体数据

f.close()

data_dict = json.loads(data)#基础数据字典

#字典取出各省数据

province_list = data_dict['RECORDS'][163::163]

# 组成各省元组列表
data_list = []#绘图需用数据
for province_data in province_list:
    province_name = province_data["provinceName"]
    province_count = province_data['confirmedCount']
    data_list.append((province_name,province_count))

# print(data_list)
map = Map()
#添加数据
map.add('各省份确诊人数',data_list,"china")
#全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国7月2号各省确诊人数"),
    visualmap_opts=VisualMapOpts(
        is_show=True,#是否显示
        is_piecewise=True,#是否分段
        pieces=[
            {'min':1,'max':50,'lable':'1-50','color':'#BBFFFF'},
            {'min':50,'max':100,'lable':'50-100','color':'#00F5FF'},
            {'min':100,'max':300,'lable':'100-300','color':'#00868B'},
            {'min':300,'max':500,'lable':'300-500','color':'#FF6A6A'},
            {'min':500,'max':1000,'lable':'500-1000','color':'#EE6363'},
            {'min':1000,'max':1500,'lable':'1000-2000','color':'#FF3030'},
            {'min':1500,'max':2000,'lable':'1000-2000','color':'#8B1A1A'},
            {'min':2000,'lable':'2000+','color':'#000000'}
        ]
    )
)
#绘图
map.render("全国疫情地图.html")



















































































































































































