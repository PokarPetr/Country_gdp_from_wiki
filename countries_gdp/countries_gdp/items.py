
import scrapy


class CountriesGdpItem(scrapy.Item):
    country_name = scrapy.Field()
    region = scrapy.Field()
    gdp = scrapy.Field()
    year = scrapy.Field()


