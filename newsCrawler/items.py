# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):
    url = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    body = scrapy.Field()