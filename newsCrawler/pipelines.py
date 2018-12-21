import pymongo
import ssl
from scrapy.conf import settings
import logging
from .spiders.utility import Utility

class NewscrawlerMongoDbPipeline(object):


    def __init__(self, mongo_db):
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_db=crawler.settings.get('MONGODB_DBNAME')
        )

    def open_spider(self, spider):
        self.collection = Utility.getNewsCollection()

    def close_spider(self, spider):
        Utility.closeDbConnection()

    def process_item(self, item, spider):
        if item['url'] is not None:
            try:
                self.collection.update_one({'url': item['url']}, {'$set': dict(item)}, upsert=True)
            except pymongo.errors.OperationFailure as e:
                logging.log(logging.ERROR, 'Failed to insert/update to MongoDB: ' + str(e.details))
        return item

    