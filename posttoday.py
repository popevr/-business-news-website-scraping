import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "posttoday"
    start_urls = []
    def __init__(self):
        url = "https://www.posttoday.com/list_content/property?page="
        for page in range(1,25):
            self.start_urls.append(url+str(page))
       
    def parse(self,response):
        news = response.css('div.item-detail h6')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()


            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('div.article-headline h2 ::text').get(),
            'content': response.css('div.article-content p ::text').getall(),
            'publish_dateime': response.css('div.date_time ::text').get(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
