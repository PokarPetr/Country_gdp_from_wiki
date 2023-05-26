import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class CountriesGdpItem(scrapy.Item):
    country_name = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    region = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    gdp = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    year = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )


