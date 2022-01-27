# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from .items import *


class SingaporeExpatsPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = connection["expats"]
        self.topicCollection = db["topics"]
        self.postCollection = db["posts"]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if isinstance(item,SingaporeExpatsPost):
                self.postCollection.insert_one(dict(item))
            elif isinstance(item,SingaporeExpatsTopic):
                self.topicCollection.insert_one(dict(item))
        return item
