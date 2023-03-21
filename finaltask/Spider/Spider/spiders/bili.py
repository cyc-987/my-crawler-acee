import scrapy


class BiliSpider(scrapy.Spider):
    name = "bili"
    allowed_domains = ["search.bilibili.com"]
    custom_settings = {'USER_AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}
    start_urls = ["https://search.bilibili.com/all?keyword=apple"]

    def parse(self, response):
        html = response.body.decode()
        filename = 'results.html'
        open(filename,'w').write(html)
        sel = Selector(response)
