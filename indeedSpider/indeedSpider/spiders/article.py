# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from indeedSpider.items import Article


class ArticleSpider(CrawlSpider):
    # The name of the spider
    name = "article"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["indeed.hk"]

    # The URLs to run on. The site maxes out at page start page 990. 
    start_urls = [f"https://www.indeed.hk/jobs?q=data+science&l=Hong+Kong&start={i}" for i in range(0, 1000, 10)]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_item method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_item"
        )
    ]

    #Spiders can take custom settings, these are higher priority then the setting.py - contains additional setting specific to this spider.
    custom_settings = {
        'DEPTH_LIMIT': 1, # this will only go one deep, come back, go to next link, and then come back, etc.
        'DOWNLOAD_DELAY' : 0.25
    }

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)


    def parse_item(self, response):

        # creating a new instance of our Article() object that will store the data that inherits from Item parent object defined in our framework (items.py)
        item = Article() 

        # passes a response into this from our crawl, and here we get the title
        title = response.xpath('//head/title/text()').getall()
        # get the content
        content = response.xpath('//div/ul/li/text()').getall()

        # This is my flag - if more than 25% of all the characters are white space, we have a problem, dump the content:
        space_percent = str(content).count(' ') / len(str(content))
        if space_percent > .25:
            content = []
        # another flag, if the content size is less than this, it must be nothing:
        elif len(str(content)) < 30:
            content = []
        # another flag, removing terms of service link:
        elif title[0] == "Cookies, Privacy and Terms of Service | Indeed.hk":
            content = []
        
        # get the string of the first title inside the list of strings
        item['title'] = title[0]
        # passing content to our item
        item['content'] = content
        
        # Tracing
        print("Title is: ", title[0])
        print("Content is: ", content)

        # only return content if we didn't dump it
        if content:
            return item