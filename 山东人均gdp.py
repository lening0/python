"""
山东省人均gdp
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("D:/python文本/shandong gdp.txt",'r',encoding="UTF-8")
data = f.read()
f.close()
data_dict = json.loads(data)

shandong_list = data_dict['山东省']

data_list = []
for shandong_data in shandong_list:
    shandong_name = shandong_data['name']
    shandong_gdp = shandong_data['gdp']
    data_list.append((shandong_name,shandong_gdp))

data_list.append(("莱芜市",104847))
map = Map()
map.add('山东人均gdp',data_list,'山东')
map.set_global_opts(
    title_opts=TitleOpts(title="山东省人均gdp"),
    visualmap_opts=VisualMapOpts(
        is_show=True,#是否显示
        is_piecewise=True,#是否分段
        pieces=[
            {"min": 150000, "label": ">15万元", "color": "#005599"},
            {"min": 120000, "max": 150000, "label": "12-15万", "color": "#0077CC"},
            {"min": 90000, "max": 120000, "label": "9-12万", "color": "#0099FF"},
            {"min": 60000, "max": 90000, "label": "6-9万", "color": "#4FBFFF"},
            {"min": 30000, "max": 60000, "label": "3-6万", "color": "#A5DFFF"},
            {"max": 30000, "label": "<3万", "color": "#E6F7FF"}

        ],
        pos_left="right",  # 图例放在右侧
        pos_top="middle"
    )
)
map.render('山东人均gdp.html')





































