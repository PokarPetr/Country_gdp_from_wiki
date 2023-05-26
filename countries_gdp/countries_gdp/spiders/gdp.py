import scrapy
from countries_gdp.items import CountriesGdpItem


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        for country in response.css('table.wikitable.sortable tbody tr:not([class])'):
            item = CountriesGdpItem()

            item['country_name'] =  country.css('td:nth-child(1) a::text').get()
            item['region'] = country.css('td:nth-child(2) a::text').get()
            item['gdp'] = country.css('td:nth-child(3)::text').get()
            item['year'] = country.css('td:nth-child(4)::text').get()

            yield item


