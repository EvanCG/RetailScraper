import scrapy
import re

from retailScraper.items import RetailScraperItem
from retailScraper.xpaths import PathsHolder

class SearchSpider(scrapy.Spider):
    name = "SearchSpider"
    allowed_domains = ["macys.org", "zales.com", "kay.com", "helzberg.com", "bluenile.com"]
    
    # Fill start_urls with text file's data here
    
    inputUrls = []
    
    while True:
        print "Enter the url of a search page #" + str(len(inputUrls) + 1) + " or enter nothing to start crawling."
        nextUrl = raw_input()
        if nextUrl == '':
            break
        inputUrls = inputUrls + [nextUrl]

    start_urls = inputUrls

    def parse(self, response):
        # Find company so you can lookup xpaths
        # Match object that contains the company
        mo = re.search(r'(?<=\.)\S+(?=\.com)', response.url)
        comp = mo.group() # Competitor
        
        # Get the custom xpaths
        productPageXPath = PathsHolder.xPaths[comp]['product']
        nextPageXPath
        
        # Send item pages to parse_item (with company in meta)
            for itemPage in response.xpath('')

        # Send next page back to parse


    def parse_item(self, response):
        item = RetailScraperItem()
        
        # Get the custom xpaths
        comp = request.meta['comp']
        titleXPath = PathsHolder.xPaths[comp]['title']
        priceXPath = PathsHolder.xPaths[comp]['price']

        item['company'] = comp # GRAB THIS FROM THE REQUEST META
        item['title'] = response.xpath(titleXPath).extract()[0]
        item['price'] = response.xpath(priceXPath).extract()[0]
        item['url'] = response.url
     
        yield item