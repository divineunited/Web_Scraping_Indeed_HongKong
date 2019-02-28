# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors import LinkExtractor

class ArticleSpider(CrawlSpider): 

    # The code in the top part of the class defines the crawling logic essentially which page to visits
    name = "article" # name - is a string which we can use to call our spider on the command line.

    allowed_domains = ["en.wikipedia.org"] # is a list of domains which we'll let our spider vist.

    start_urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29"] # url of the page or pages to start on.
    
    # The rule object takes a LinkExtractor and two other arguments. The callback argument takes a function which will be called on each page to excute our parsing logic (which is our parse_item function defined below). And the final argument follow which is a boolean which specifies if links should be followed from each response extracted, it defualts to True.
    rules = [ 
        #Link extractor uses a regex to define which links to follow - this will match the links we wish to extract.
        Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),), callback="parse_item", follow=True)
    ]


    #Spiders can take custom settings, these are higher priority then the setting.py - contains additional setting specific to this spider.
    custom_settings = {
        'DEPTH_LIMIT': 1, # this will only go one deep, come back, go to next link, and then come back, etc.
        'DOWNLOAD_DELAY' : 0.25
    }

    # parse_item is the parsing logic, what items in that page are we interested in.
    def parse_item(self, response):
        '''When it goes to a new website, this is what I do to scrape this webpage.'''

        # creating a new instance of our Article() object that will store the data that inherits from Item parent object defined in our framework (items.py)
        item = Article() 

        # passes a response into this from our crawl, and here we get the title
        title = response.css('#firstHeading::text').extract_first()
        # get the content
        content =  response.css('#toc *::text').extract()
        print("Title is: "+title)
        item['title'] = title
        item['content'] = content
        return item