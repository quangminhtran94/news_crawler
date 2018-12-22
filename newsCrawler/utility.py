from scrapy.conf import settings
import pymongo
import ssl

class Utility(object):
    HTTP_PREFIX = 'http://'

    HTTPS_PREFIX = 'https://'

    @staticmethod
    def convertToValidUrl(url):
        if not url.startswith(Utility.HTTP_PREFIX) and not url.startswith(Utility.HTTPS_PREFIX):
            return ''.join([Utility.HTTP_PREFIX, url])
        return url

    @staticmethod
    def getDbConnection():
        if settings['LOCAL_MODE']:
            return pymongo.MongoClient(settings['MONGODB_LOCAL_HOST'])
        return pymongo.MongoClient(settings['MONGODB_HOST'])

    @staticmethod
    def closeDbConnection(client):
        client.close()