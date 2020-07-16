# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesinfospiderItem(scrapy.Item):
    # define the fields for your item here like:
    电影 = scrapy.Field()
    类型 = scrapy.Field()
    上映时间 = scrapy.Field()
