import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "ndtv"
    start_urls = []
    def __init__(self):
        url = "https://www.ndtv.com/business/latest/page-"
        for page in range(1,14):
            self.start_urls.append(url+str(page))

    def parse(self,response):
        news = response.css('h2.newsHdng')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()

            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('h1.sp-ttl::text').get(),
            'content': response.css('p::text').getall(),
            'publish_dateime': response.css('span.pst-by_lnk span::text').get().strip(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
