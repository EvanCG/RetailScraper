# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

# Removes whitespace from the title text at the edges of a title.
class CleanTitleText(object):
    def process_item(self, item, spider):
        if item['title']:
            item['title'] = item['title'].strip()
        return item

# Strip out non-price text from string
# Raw string could have text (ex: 'Sale $99.99')
class CleanPriceText(object):
    def process_item(self, item, spider):
        if item['price']:
            rawPriceString = item['price']
            noCommaString = rawPriceString.replace(",","")        
            item['price'] = re.search(r'\d+(\.\d\d)?', noCommaString).group(0)
        return item