from scrapy.spiders import CrawlSpider, Rule
from newsCrawler.items import ArticleItem
from scrapy.linkextractors import LinkExtractor
from .utility import Utility
from urllib.parse import urlparse
import re
class NewsSpider(CrawlSpider):

    TYPE_XPATH = "//meta[@property='og:type']/@content"
    ARTICLE_TYPE = "article"

    AUTHOR_XPATH = "//meta[@property='article:author']/@content"

    TITLE_XPATH = "//meta[@property='og:title']/@content"

    DESCRIPTION_XPATH = "//meta[@property='og:description']/@content"

    BODY_XPATH = "//div[@itemprop='articleBody' or @property='articleBody']/p"

    name="news_spider"
    rules = (
        Rule(
            link_extractor = LinkExtractor(allow=(), unique=True),
            callback='parse_article',
            follow=True
        ),
    )

    def __init__(self, start_url=None, url_file_path=None):
        super(NewsSpider, self).__init__()

        if start_url:
            self.start_urls=[Utility.convertToValidUrl(start_url)]
        elif url_file_path:
            self.start_urls=[]
            with open(url_file_path, 'r') as url_file:
                for line in url_file.readlines():
                    self.start_urls.append(line.strip())
        self.allowed_domains = [urlparse(url).hostname.lstrip('www.') for url in self.start_urls]

    def parse_article(self, response):
        page_type = response.xpath(NewsSpider.TYPE_XPATH).extract_first()
        if page_type == NewsSpider.ARTICLE_TYPE:
            article_item = ArticleItem()
            article_item['url'] = response.url
            article_item['author'] = response.xpath(NewsSpider.AUTHOR_XPATH).extract_first()
            article_item['title'] = response.xpath(NewsSpider.TITLE_XPATH).extract_first()
            article_item['description'] = response.xpath(NewsSpider.DESCRIPTION_XPATH).extract_first()
            article_item['body'] = re.sub(re.compile('<.*?>'), '', ' '.join(response.xpath(NewsSpider.BODY_XPATH).extract()))
            return article_item

        
