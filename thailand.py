import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "thailand"
    start_urls = []
    def __init__(self):
        url = "https://thailand-property-news.knightfrank.co.th/category/ข่าวอสังหา/page/"
        for page in range(1,15):
            self.start_urls.append(url+str(page))
       
    def parse(self,response):
        news = response.css('div.td_module_3 h3.entry-title')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()


            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('h1.entry-title ::text').get(),
            'content': response.css('div.td-post-content p ::text').getall(),
            'publish_dateime': response.css('span.td-post-date time ::text ').get(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
