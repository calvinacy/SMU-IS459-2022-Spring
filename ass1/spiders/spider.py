import scrapy
from ..items import *

class ExpatSpider(scrapy.Spider):
    name = 'expatspider'

    start_urls = [
        'https://forum.singaporeexpats.com/viewforum.php?f=93',
    ]

    def parse(self, response):
        for topic_list in response.xpath('//ul[@class="topiclist topics"]'):
            for topic in topic_list.xpath('li/dl'):
                topic_item = SingaporeExpatsTopic()
                topic_item['topic'] = topic.xpath('dt/div/a/text()').get()
                topic_item['no_of_replies'] = topic.xpath('dd[@class="posts"]/text()').get().strip()
                topic_item['no_of_views'] = topic.xpath('dd[@class="views"]/text()').get().strip()
                yield topic_item
                yield response.follow(topic.xpath('dt/div/a/@href').get(), \
                    self.parse)
                    
        for post in response.xpath('//div[@id="page-body"]/div[contains(@class, "post has-profile")]/div[has-class("inner")]'):
            post_item = SingaporeExpatsPost()
            post_item['post'] = response.xpath('//h2[@class="topic-title"]/a/text()').get()
            post_item['author'] = post.xpath('//*[@class="author"]/span/strong/a/text()').get()
            post_item['content'] = post.xpath('div[@class="postbody"]/div/div[@class="content"]/text()').get()
            yield post_item
        
        next_page = response.xpath('//li[has-class("arrow next")]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
