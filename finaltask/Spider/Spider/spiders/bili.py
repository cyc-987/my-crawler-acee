import scrapy
import re
import js2xml
import json
from Spider.items import biliitem


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["search.bilibili.com"]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
        'Cookie':'sid=h736xd04; CURRENT_FNVAL=4048; b_nut=1679410216; buvid3=AE749284-2340-82AC-5DBF-5FBA327DDC9816277infoc; buvid4=D712FC9F-6480-AEFA-5D5C-2A14D249D44B16277-023032122-yW9JSiNaa2qy6iFsxeTV3A%3D%3D; _uuid=10D46482D-DEDD-E54E-3488-537929C2BD9D15119infoc; b_lsid=1A1533E8_18704A638C9; buvid_fp=86dd4f964017c6ac8f7046ba10e52762; nostalgia_conf=-1'}
    start_urls = ["https://search.bilibili.com/all?keyword=ikun&page=%s&o=30"%s for s in range(1,35)]
    


    def parse(self, response):
        
        html = response.body.decode('utf-8')
        filename = 'results.html'
        open(filename,'w').write(html)
        
        data = response.xpath('/html/body/script[2]/text()').extract()
        dataselected = re.findall(r'{type:d,id:.{0,1000},biz_data:c}',str(data))
        open('data.html','w').write(str(dataselected))
        

        
        for each in dataselected:
            item = biliitem()

            #plays = each.xpath('div/div[2]/a/div/div[2]/div/div/span[1]/span/text()').extract()
            #name = each.xpath('div/div[2]/div/div/a/h3/@title').extract()
            #href = each.xpath('div/div[2]/div/div/a/@href').extract()

            #item['plays'] = plays[0]
            #item['name'] = name[0]
            #item['href'] = href[0]
            
            
            bvid = re.search(r'bvid:"([0-9a-zA-Z]*)",',each).group(1)
            '''
            title = re.search(r'title:"(.*)",',each).group(1)
            description = re.search(r'description:"(.*)",',each).group(1)
            play = re.search(r',play:([0-9]*),',each).group(1)
            like = re.search(r'like:([0-9]*),',each).group(1)
            favorites = re.search(r'favorites:([0-9]*),',each).group(1)
            tag = re.search(r'tag:"(.*)",',each).group(1)
            duration = re.search(r'duration:"([0-9]*:[0-9]*)",',each).group(1)
            '''
            
            item['bvid'] = bvid
            '''
            item['title'] = title
            item['description'] = description
            item['play'] = play
            item['like'] = like
            item['duration'] = duration
            item['favorites'] = favorites
            item['tag'] = tag
            '''

            yield item

            # items.append(item)
        # return items
