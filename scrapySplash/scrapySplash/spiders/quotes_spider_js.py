import scrapy


class QuotesSpiderJsSpider(scrapy.Spider):
    name = 'quotes_spider_js'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
