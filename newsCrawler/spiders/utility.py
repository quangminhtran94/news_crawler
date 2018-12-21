from scrapy.conf import settings
import pymongo

class Utility(object):
    HTTP_PREFIX = 'http://'

    HTTPS_PREFIX = 'https://'

    client = pymongo.MongoClient(settings['MONGODB_HOST'])

    @staticmethod
    def convertToValidUrl(url):
        if not url.startswith(Utility.HTTP_PREFIX) and not url.startswith(Utility.HTTPS_PREFIX):
            return ''.join([Utility.HTTP_PREFIX, url])
        return url

    @staticmethod
    def getNewsCollection():
        db = Utility.client[settings['MONGODB_DBNAME']]
        return db[settings['MONGODB_NEWS_COLLECTION']]

    @staticmethod
    def closeDbConnection():
        Utility.client.close()