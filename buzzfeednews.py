import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "buzzfeednews"
    start_urls = []
    def __init__(self):
        url = "https://www.buzzfeednews.com/us/feed/section/business?page="
        for page in range(1,3):
            self.start_urls.append(url+str(page))
      
    def parse(self,response):
        news = response.css('article.newsblock-story-card h2 ')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()

            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        yield{
            'title': response.css('h1.news-article-header__title::text').get(),
            'content': response.css('div.subbuzz p::text').getall(),
            'publish_dateime': response.css('div.news-article-header__timestamps p::text').get().strip(),
            'source_url': response.request.meta['source_url'],
            'date':date1
        }
