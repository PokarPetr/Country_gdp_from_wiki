import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item["gdp"], float):
            raise DropItem("Missing GDP value. Item excluded")

        return item

class SaveToDatabasePipeline:
    def __init__(self):
        self.con = sqlite3.connect("countries_gdp.db")
        self.cur = self.con.cursor()

    def open_spider(self, spider):
        self.cur.execute("""CREATE TABLE IF NOT EXIST countries_gdp(
        countries_name TEXT PRIMARY KEY, 
        region TEXT, 
        gdp REAL, 
        year INTEGER)
        """)
        self.con.commit()

    def process_item(self, item, spider):
        pass