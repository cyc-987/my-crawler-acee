import re
import requests
from bs4 import BeautifulSoup as bs
import lxml

str = '<a data-v-62a02286="" href="//www.bilibili.com/video/BV1ZT411D7Zw/" target="_blank"><h3 class="bili-video-card__info--tit" data-v-62a02286="" title="【网梗课代表】114514是什么梗？">【网梗课代表】<emclass="keyword">114514</em>是什么梗？</h3></a>'
soup = bs(str,features='lxml')
print(soup.h3['id'])