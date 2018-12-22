# Crawler using Scrapy
For Isentia interview process
  - Scrapy framework for crawler
  - Flask for providing API
  - MongoDB for storing data crawled

# Solution

  - Spider implementation to extract article from BBC using Xpath with Scrapy
  - Data craweled is store in MongoDB hosted in compose.com
  - Flask provided basic API for searching: 
    ```
    /news/search/<keyword>?prePageState=<prePageState>&fetchSize=<fetchSize>
    ```
    *prePageState* is to mark the position of last result returned, will set to *None* for last result page
    *fetchSize* is size of 1 resultPage

Note to improve:
  - Data should be store in searching-purpose storage, such as Elasticsearch to support better ranking and search API
  - More test cases to be covered
  - Dependency Injection should be done better (due to the fact that I am quite new for Python)

# Requirements
  - Run with Python 3
  - Install requirements
    ```
    pip install -r requirements.txt
    ```

# Usage
  - Crawl data:
    ```
    $ scrapy crawl news_spider -a start_url=https://www.bbc.com/news/uk-england-sussex-46623754
    ```
  - Start API:
    ```
    $ cd newsCrawler
    $ python api.py
    ```
  - Access API via url:
    ```
    http://localhost:5000/news/search/tens?prePageState=4
    ```
    In this example, search for *tens* and *prePageState* is 4, *fetchSize* will use default value