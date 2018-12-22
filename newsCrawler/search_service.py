import abc
from utility import Utility
from pymongo.errors import OperationFailure
import logging
from scrapy.conf import settings
from flask import jsonify

class SearchService(abc.ABC):
    _instance = None
    @abc.abstractmethod
    def search(self, keyword, prePageState, fetchSize):
        pass

    #better use IOC framework to manage this. for limited time I directly put it in method args
    @staticmethod
    def getInstance(newsCollection = None):
        if(SearchService._instance is not None):
            return SearchService._instance
        SearchService._instance = SearchServiceImpl()
        if newsCollection is None:
            dbClient = Utility.getDbConnection()
            db = dbClient[settings['MONGODB_DBNAME']]
            SearchService._instance.collection = db[settings['MONGODB_NEWS_COLLECTION']]
        else:
            SearchService._instance.collection = newsCollection
        return SearchService._instance

class SearchServiceImpl(SearchService):
    def search(self, keyword, prePageState, fetchSize):
        results = []
        if keyword is not None:
            try:
                for item in self.collection.find({"$text": {"$search": keyword}}):
                    results.append({
                        'url': item['url'],
                        'title': item['title'],
                        'description': item['description'],
                        'body': item['body'],
                        'author': item['author'],
                    })
            except OperationFailure as e:
                logging.log(logging.ERROR, 'Failed loading from MongoDB: ' + str(e.details))
        response = {
            'result' : results,
            'prePageState' : prePageState + len(results)
        }
        response = jsonify(results)
        return response