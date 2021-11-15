import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "japan"
    start_urls = []
    def __init__(self):
        url = "https://www.japantimes.co.jp/news/business/page/"
        for page in range(1,170):
            self.start_urls.append(url+str(page))

    def parse(self,response):
        news = response.css('div.main_content header p')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()

            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('h1::text').get(),
            'content': response.css('div.padding_block p::text').getall(),
            'publish_dateime': response.css('div.meta-right time::text').get().strip(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
