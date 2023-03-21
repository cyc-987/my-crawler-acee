import re
import requests
import json
from bs4 import BeautifulSoup as bs
import lxml
'''
i = 1
for x in range(1,20):
    temp_str = 'div[' + str(i) + ']/div/div[2]/'
    i = i + 1
    print(temp_str)
'''
'''
str = 'bvid:"BV1Lj411V79A"'
result = re.search(r'bvid:"([0-9a-zA-Z]*)"',str)
print(result.group(1))
'''

str = '{type:d,id:bJ,author:"玛丽莲萌露lulu",mid:11714449,typeid:i,typename:j,arcurl:"http:\\\\u002F\\\\u002Fwww.bilibili.com\\\\u002Fvideo\\\\u002Fav394797844",aid:bJ,bvid:"BV1co4y1Y79J",title:"【\\\\u003Cem class=\\\\"keyword\\\\"\\\\u003Eikun\\\\u003C\\\\u002Fem\\\\u003E破防】285\\\\u002F911高材生\\\\u003Cem class=\\\\"keyword\\\\"\\\\u003Eikun\\\\u003C\\\\u002Fem\\\\u003E不堪辱骂，穿上和服准备移民日本，祖国将损失高级人才",description:"都怪你们小黑子逼走了高材生ikun，害得祖国损失高级人才！",arcrank:e,pic:"\\\\u002F\\\\u002Fi2.hdslb.com\\\\u002Fbfs\\\\u002Farchive\\\\u002Fef5b7c6200ed081981edc62de1b430524938c8c0.jpg",play:258211,video_review:bK,favorites:1384,tag:"ikun,真爱粉,小黑子,蔡徐坤,和服",review:741,pubdate:1676969949,senddate:1678155955,duration:"0:44",badgepay:f,hit_columns:[g,m,h],view_type:a,is_pay:b,is_union_video:b,rec_tags:c,new_rec_tags:[],rank_score:104750333,like:13557,upic:"https:\\\\u002F\\\\u002Fi1.hdslb.com\\\\u002Fbfs\\\\u002Fface\\\\u002F40292911010d902fdd54df1f1334bf67116d5ce4.jpg",corner:a,cover:a,desc:a,url:a,rec_reason:a,danmaku:bK,biz_data:c}'
data = eval(str)
print(type(data))
