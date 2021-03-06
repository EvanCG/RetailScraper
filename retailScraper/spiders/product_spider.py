import scrapy
import re

from retailScraper.items import RetailScraperItem
from retailScraper.xpaths import PathsHolder

class ProductSpider(scrapy.Spider):
    name = "ProductSpider"
    allowed_domains = ["macys.org", "zales.com", "kay.com", "helzberg.com", "bluenile.com"]
    
    # Fill start_urls with text file's data here
    
    fname = raw_input('Please enter a text file to search: ')

    # Open the input text file and strip each line while reading the urls that are available
    with open(fname, "rb") as ins:
        array = []
        for line in ins:
            line = line.strip()
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