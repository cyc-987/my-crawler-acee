import scrapy
from Spider.items import biliitem

class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["search.bilibili.com"]
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    start_urls = ["https://search.bilibili.com/all?keyword=ikun"]

    def parse(self, response):
        html = response.body.decode()
        filename = 'results.html'
        open(filename,'w').write(html)
        
        test = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[1]/div/div')
        open('testtemp.html','w').write(str(test))
                
        items = []
        i = 1
        for each in response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[1]/div/div'):
            #open('testtemp.html','w').write(str(each))
            item = biliitem()
            i = i + 1
            plays = each.xpath('div/div[2]/a/div/div[2]/div/div/span[1]/span/text()').extract()
            name = each.xpath('div/div[2]/div/div/a/h3/@title').extract()
            href = each.xpath('div/div[2]/div/div/a/@href').extract()
            
            item['plays'] = plays[0]
            item['name'] = name[0]
            item['href'] = href[0]
            
            items.append(item)
            pass
        return items

