import scrapy


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["search.bilibili.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=apple"]

    def parse(self, response):
        filename = 'results.html'
        open(filename,'w').write(response.body)
        pass
