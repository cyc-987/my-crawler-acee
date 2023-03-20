'''
子节点是tag下一级所属节点,包括内容
子孙节点是tag所有下级节点,包括内容
父节点是tag上一级节点,最上到soup对象
.parents递归输出所有父节点
兄弟节点顾名思义,前后同级节点,特别注意标签之间的字符串也算同级节点
.next_element指向下一个被解析对象,注意区别.next_sibling
'''

import re
import requests
from bs4 import BeautifulSoup as bs
import lxml

#构建url
url = "https://search.bilibili.com/all?keyword=114514"#关键词可以在这里改
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
           ,"Host":"search.bilibili.com"
           ,"Connection":"keep-alive"
           ,"Cookie":"CURRENT_FNVAL=4048; sid=6hxt4adl; nostalgia_conf=-1; buvid_fp=86dd4f964017c6ac8f7046ba10e52762; _uuid=142810DF3-E26D-F3F7-374E-A3C72C966C8488516infoc; b_lsid=CC10EE944_186FFB1CF7E; b_nut=1679327088; b_ut=7; buvid3=DF53DFC1-B513-9179-774F-44E77A0AB76D88237infoc; buvid4=2FE31C40-8E86-6F71-11DF-10CF5B6901B888917-023032023-yW9JSiNaa2qy6iFsxeTV3A%3D%3D; header_theme_version=undefined; home_feed_column=5; i-wanna-go-back=-1; innersign=0"}

res = requests.get(url,headers=headers)
print(res)#打印请求情况
html = res.content.decode()
soup = bs(html,features='lxml')#创建soup示例
with open ("return.html","w",encoding='utf-8') as f:
    f.write(html)

#对soup示例进行操作
'''
def selet_bilihref_with_id(tag):
    return tag.has_attr('href') and tag.has_attr('id')
result = soup.find_all(selet_bilihref_with_id)
'''
result = soup.find_all('a',href = re.compile(r'.*www\.bilibili\.com/video/BV[0-9a-zA-Z]+.*'), attrs={'data-v-62a02286':True})

#二次筛选
result = str(result)
for_select = bs(result,features='lxml')
result_selected = for_select.find_all('h3')
for temp in result_selected:
    print(temp['title'])
    print(temp.parent['href'],end='\n')
#b站的tag貌似没有同时具备href链接和id属性的，我用输出搜索结果第一页代替了