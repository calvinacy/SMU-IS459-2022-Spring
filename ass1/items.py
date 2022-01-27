# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SingaporeExpatsTopic(scrapy.Item):
    # define the fields for your item here like:
    topic = scrapy.Field()
    no_of_replies = scrapy.Field()
    no_of_views = scrapy.Field()
    

class SingaporeExpatsPost(scrapy.Item):
    # define the fields for your item here like:
    post = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    