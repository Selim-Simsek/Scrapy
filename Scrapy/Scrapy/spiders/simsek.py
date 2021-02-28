import scrapy


class SimsekSpider(scrapy.Spider):
    name = 'simsek'
    allowed_domains = ['selimsimsek.com']
    custom_settings={
    'FEED_URI': 'data.json',
    'FEED_FORMAT': 'json'
    }


    def start_requests(self):
    	url='http://selimsimsek.com/'
    	yield scrapy.Request(url)
    	

    def parse(self, response):
        yield {'Response':response.selector.xpath('.//div[@class="skill-bar-percent"]/text()').extract()}
