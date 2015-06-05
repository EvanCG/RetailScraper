# -*- coding: utf-8 -*-

# Scrapy settings for retailScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'retailScraper'

SPIDER_MODULES = ['retailScraper.spiders']
NEWSPIDER_MODULE = 'retailScraper.spiders'

ITEM_PIPELINES = ['retailScraper.pipelines.CleanTitleText', 'retailScraper.pipelines.CleanPriceText']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'retailScraper (+http://www.yourdomain.com)'
