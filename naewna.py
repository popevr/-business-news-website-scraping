import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "naewna"
    start_urls = []
    def __init__(self):
        url = "https://www.naewna.com/ajax_newslist.php?cat=business&ids=&limit=11&page="
        for page in range(1,428):
            self.start_urls.append(url+str(page))
       
    def parse(self,response):
        news = response.css('div.col-xs-6 h3')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()


            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('div.col-md-9 div.newscontent h1::text').get(),
            'content': response.css('div.newsdetail p::text').getall(),
            'publish_dateime': response.css('div.newscontent div.newsdate::text').get(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
