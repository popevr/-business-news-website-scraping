import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "foxbusiness"
    start_urls = []
    def __init__(self):
        url = "https://www.foxbusiness.com/category/business-leaders?page="
        for page in range(1,100):
            self.start_urls.append(url+str(page))

    def parse(self,response):
        urlss = 'https://www.foxbusiness.com'
        news = response.css('h3.title')
        for a in news :
            link1 = a.css('a::attr(href)').get()
            link = urlss + str(link1)
            source1 = a.css('a::attr(href)').get()
            source = urlss + str(source1)

            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('h1::text').get(),
            'content': response.css('div.article-body p::text').getall(),
            'publish_dateime': response.css('div.article-date time::text').get().strip(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
