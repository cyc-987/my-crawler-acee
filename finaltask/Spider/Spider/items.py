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
    plays = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()