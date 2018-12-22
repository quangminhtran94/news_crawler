import unittest
import os
import sys
from ..spiders.bbc_news_spider import NewsSpider

from scrapy.http import Response, Request
import os

class SpiderTest(unittest.TestCase):

    MOCK_URL = 'http://mockurl.com'

    def setUp(self):
        self.spider = NewsSpider()

    def test_parse(self):
        item = self.spider.parse_item(generateMockResponse('sample_doc/sample_doc_1.html'))
        self.assertIsNotNone(item)
        self.assertIsNotNone(item['body'])
        self.assertEqual(item['url'], SpiderTest.MOCK_URL)

    #test cases should cover all exceptions from parsing
    def test_parse_empty_body(self):
        pass

    def generateMockResponse(self, pathToFile):
        request = Request(url = SpiderTest.MOCK_URL)
        filePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), pathToFile)
        mockBody = open(filePath, 'r').read()
        return Response(url = SpiderTest.MOCK_URL, request=request, body= mockBody)

if __name__ == "__main__":
    unittest.main()