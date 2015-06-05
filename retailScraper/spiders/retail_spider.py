import scrapy
import re

from retailScraper.items import RetailScraperItem
from retailScraper.xpaths import PathsHolder

class RetailSpider(scrapy.Spider):
    name = "rtspider"
    allowed_domains = ["macys.org", "zales.com", "kay.com", "helzberg.com", "bluenile.com"]
    
    # Fill start_urls with text file's data here
    
    # File Name
    fname = raw_input('Please enter a text file to search: ')
    
    with open(fname, "rb") as ins:
        array = []
        for line in ins:
            array.append(line)
        
    start_urls = array
    
    def parse(self, response):
        item = RetailScraperItem()
        # Find company so you can lookup xpaths
        # Match object that contains the company
        mo = re.search(r'(?<=\.)\S+(?=\.com)', response.url)
        
        # Competitor
        comp = mo.group()
        
        titleXPath = PathsHolder.xPaths[comp]['title']
        priceXPath = PathsHolder.xPaths[comp]['price']

        item['company'] = comp        
        item['title'] = response.xpath(titleXPath).extract()[0]
        item['price'] = response.xpath(priceXPath).extract()[0]
        item['url'] = response.url
     
        yield item