import scrapy
from countries_gdp.items import CountriesGdpItem
from scrapy.loader import ItemLoader


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        for country in response.css('table.wikitable.sortable tbody tr:not([class])'):

            item = ItemLoader(item=CountriesGdpItem(), selector=country)
            item.add_css('country_name', 'td:nth-child(1) a')
            item.add_css('region', 'td:nth-child(2) a')
            item.add_css('gdp', 'td:nth-child(3)')
            item.add_css('year', 'td:nth-child(4)')
            yield item.load_item()


