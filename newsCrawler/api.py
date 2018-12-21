from pymongo import MongoClient
from pymongo.errors import OperationFailure
import pymongo
from flask import Flask, jsonify, request
from scrapy.utils.project import get_project_settings
from utility import Utility
import ssl
import logging

app = Flask(__name__)

#/news/search/<keyword>?prePageState=<prePageState>&fetchSize=<fetchSize>
@app.route('/news/search/<keyword>', methods=['GET'])
def get_news(keyword):
    collection = Utility.getNewsCollection()
    results = []
    # prePageState and fetchSize is ONLY for illustration purpose only
    # they will be used in more advanced search framework like Elasticsearch
    prePageState = int(request.args.get('prePageState', 0))
    fetchSize = int(request.args.get('fetchSize', 5))
    
    if keyword is not None:
        try:
            for item in collection.find({"$text": {"$search": keyword}}):
                results.append({
                    'url': item['url'],
                    'title': item['title'],
                    'description': item['description'],
                    'body': item['body'],
                    'author': item['author'],
                })
        except OperationFailure as e:
            logging.log(logging.ERROR, 'Failed loading from MongoDB: ' + str(e.details))

    # prePageState in first search is equal to 0
    # reponse will not have prePageState for last result batch
    response = {
        'result' : results,
        'prePageState' : prePageState + len(results)
    }
    response = jsonify(results)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
