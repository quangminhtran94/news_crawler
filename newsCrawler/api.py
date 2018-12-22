from pymongo import MongoClient
from pymongo.errors import OperationFailure
import pymongo
from flask import Flask, jsonify, request
from scrapy.utils.project import get_project_settings
from search_service import SearchService
import ssl
import logging

app = Flask(__name__)

#/news/search/<keyword>?prePageState=<prePageState>&fetchSize=<fetchSize>
@app.route('/news/search/<keyword>', methods=['GET'])
def get_news(keyword):
    # prePageState and fetchSize is ONLY for illustration purpose only
    # they will be used in more advanced search framework like Elasticsearch
    prePageState = int(request.args.get('prePageState', 0))
    fetchSize = int(request.args.get('fetchSize', 5))
    
    searchService = SearchService.getInstance()
    return searchService.search(keyword, prePageState, fetchSize)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
