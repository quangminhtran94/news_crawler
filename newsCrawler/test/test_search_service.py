import unittest
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
from ..search_service import SearchService

class TestSearchService(unittest.TestCase):
    NOT_FOUND_KEYWORD = "!@#$"

    FOUND_KEYWORD = "Mock"

    def setUp(self):
        settings = get_project_settings()
        self.dbConnection = MongoClient(settings['MONGODB_LOCAL_HOST'])
        db = self.dbConnection[settings['MONGODB_DBNAME']]
        mockItem = {
            'url': 'http://mockurl.com/',
            'title': 'Mock Article Item',
            'body': 'Mock body'
        }
        self.collection = db[settings['MONGODB_NEWS_COLLECTION']]
        self.collection.insert_one(mockItem)

    def tearDown(self):
        self.collection.delete_one({'url' : 'http://mockurl.com/'})
        self.dbConnection.close()

    def test_result_found(self):
        searchService = SearchService.getInstance(self.collection)
        result = searchService.search(keyword = TestSearchService.FOUND_KEYWORD)
        self.assertEqual(len(result.result), 1)
        self.assertEqual(result.prePageState, 1)

    def test_result_not_found(self):
        searchService = SearchService.getInstance(self.collection)
        result = searchService.search(keyword = TestSearchService.NOT_FOUND_KEYWORD)
        self.assertEqual(len(result.result), 0)
        self.assertEqual(result.prePageState, 0)

if __name__ == "__main__":
    unittest.main()