# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

'''
class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
'''

class biliitem(scrapy.Item):
    bvid = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    play = scrapy.Field()
    like = scrapy.Field()
    favorites = scrapy.Field()
    tag = scrapy.Field()
    duration = scrapy.Field()
    
    
    pass