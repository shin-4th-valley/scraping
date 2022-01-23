import scrapy
from scrapy_splash import SplashRequest

class QuotesSpiderJsSpider(scrapy.Spider):
    name = 'quotes_spider_js'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url = url, callback = self.parse, endpoint = "render.html")

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            author = quote.xpath('.//*[@class="author"]/text()').get()
            quote = quote.xpath('.//*[@class="text"]/text()').get()
            yield {'author': author,
                   'quote': quote}

        # レンダリングされたHTMLなので、これでも問題ない
        # next_page_url = response.xpath('//*[@class="next"]/a/@href').get()
        # abs_next_page_url = response.urljoin(next_page_url)
        # if abs_next_page_url is not None:
        #     yield SplashRequest(abs_next_page_url, callback=self.parse)

        # Lua Scriptバージョン
        # URLに移動し、Nextボタンをクリックし、次のページのURLとHTMLを返す
        script = """function main(splash)
                assert(splash:go(splash.args.url))
                splash:wait(1)
                button = splash:select("li[class=next] a")
                splash:set_viewport_full()
                splash:wait(1)
                button:mouse_click()
                splash:wait(1)
                return {url = splash:url(),
                        html = splash:html()}
            end"""

        yield SplashRequest(url=response.url,
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source': script})

