import scrapy
import datetime
date1 = datetime.datetime.now()
class QuotesSpider(scrapy.Spider):
    name = "work"
    def start_requests(self):
        urls = [
            "http://203.155.220.117:8080/BMAWWW/html_statistic/report.php"    
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
       
    def parse(self,response):
        news = response.css('ul.gallery_kat tr td ')
        for a in news :
            link = a.css('a::attr(href)').get()
            source = a.css('a::attr(href)').get()
            if link == 'javascript:void(0);':
                continue


            yield response.follow(url=link, callback=self.parse_categories,meta = {'source_url':source})

    def parse_categories(self,response):
        
        
        yield{
            'ชื่อเขต': response.css('td.head_work_font ::text').get(),
            '':response.css('td p span::text').getall()
        }
