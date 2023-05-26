import scrapy


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://wikipedia.org/"]

    def parse(self, response):
        pass
