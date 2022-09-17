#!/usr/bin/python3

import plotly.express as px
import json
import pandas as pd


filename = 'data/eq_data_30_day_m1.json'

with open(filename) as f:
    all_eq_data = json.load(f)
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)
all_eq_dict = all_eq_data['features']
# print(len(all_eq_dict))

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
data=pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['jingdu', 'weidu', 'weizhi', 'zhengji']
)
data.head()


fig = px.scatter(
    data,
    x='jingdu',
    y='weidu',
    # labels={'x':'jingdu','y':'weidu'},
    range_x=[-200, 200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='world eq',
    size='zhengji',
    size_max=10,
    color='zhengji',
    hover_name='weizhi'
)

fig.write_html('global_eq.html')
fig.show()