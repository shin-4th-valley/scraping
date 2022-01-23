import scrapy
from scrapy_splash import SplashRequest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


class YuryoSpiderJsSpider(scrapy.Spider):
    name = 'yuryo_spider_js'
    allowed_domains = ['jinzai.hellowork.mhlw.go.jp']
    start_urls = ['https://jinzai.hellowork.mhlw.go.jp/JinzaiWeb/GICB101010.do?screenId=GICB101010&action=initDisp']

    def start_requests(self):
        # browser = webdriver.Chrome()
        # browser.implicitly_wait(3)

        # first_url = "https://jinzai.hellowork.mhlw.go.jp/JinzaiWeb/GICB101010.do?action=initDisp&screenId=GICB101010"
        # browser.get(first_url)
        # time.sleep(1)
        # print("accessed home page")

        # btn = browser.find_element(by=By.XPATH, value='/html/body/div/div/form/div[2]/div[2]/div/div/dl[1]/dt[2]/a')
        # time.sleep(1)
        # btn.click()
        # print("accessed list page")

        # checkbox_all_pref = browser.find_element(by=By.ID, value='ID_cbZenkoku1')
        # time.sleep(1)
        # checkbox_all_pref.click()
        # print(checkbox_all_pref.is_selected())
        # time.sleep(1)

        # checkbox_yuryo_shokugyo = browser.find_element(by=By.ID, value='ID_cbJigyoshoKbnYu1')
        # time.sleep(1)
        # checkbox_yuryo_shokugyo.click()
        # print(checkbox_yuryo_shokugyo.is_selected())
        # time.sleep(3)

        # btn_to_filter = browser.find_element(by=By.XPATH, value='/html/body/form/div[2]/div[3]/div/div[3]/input')
        # btn_to_filter.click()
        # print("filter with targeted category")

        for url in self.start_urls:
            yield SplashRequest(url = url, callback = self.parse, endpoint = "render.html")

    def parse(self, response):
        table = response.xpath('//*[@id="search"]')[0]
        print(table)
        trs = table.xpath('.//tr')[3:]
        print(trs)
        for tr in trs:
            kyoka_url = tr.xpath('.//td[1]/text()').get().strip()
            kyoka_num = tr.xpath('.//td[2]/text()').get().strip()
            # kyoka_date = tr.xpath('.//td[2]/text()').get().strip()
            # name = tr.xpath('.//td[3]/text()').get().strip()
            # name_2 = tr.xpath('.//td[4]/text()').get().strip()
            # phone = tr.xpath('.//td[5]/text()').get().strip()
            # phone_3 = tr.xpath('.//td[6]/text()').get().strip()
            # more_than_4 = tr.xpath('.//td[7]/text()').get().strip()
            # more_than_4_and_yuki_muki = tr.xpath('.//td[8]/text()').get().strip()
            # less_muki = tr.xpath('.//td[8]/text()').get().strip()
            # more_than_4_and_yuki_muki = tr.xpath('.//td[8]/text()').get().strip()
            # unknown = tr.xpath('.//td[8]/text()').get().strip()
            # tesuryo = tr.xpath('.//td[8]/text()').get().strip()
            # henkin = tr.xpath('.//td[8]/text()').get().strip()
            # shosai_joho = tr.xpath('.//td[8]/text()').get().strip()

            yield {
                "許可・受理番号_／許可年月日・_届出受理年月日（URL）": kyoka_url,
                "許可・受理番号_／許可年月日・_届出受理年月日": kyoka_num,
                # "許可・受理番号_／許可年月日・_届出受理年月日1": kyoka_date,
                # "事業主氏名_／事業所名称": name,
                # "事業主氏名_／事業所名称2": name_2,
                # "事業所所在地_／電話番号": phone,
                # "事業所所在地_／電話番号3": phone_3,
                # "4か月以上有期及び無期（人）": more_than_4,
                # "4か月以上有期及び無期（人）うち無期（人）": more_than_4_and_yuki_muki,
                # "無期雇用のうち６か月以内離職者数_（人）": less_muki,
                # "判明せず_（人）": unknown,
                # "手数料": tesuryo,
                # "返戻金制度": henkin,
                # "詳細情報（URL）": shosai_joho,
            }

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
