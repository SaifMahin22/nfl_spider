# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NflItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    position = scrapy.Field()
    table_header = scrapy.Field()
    log_year = scrapy.Field()
    URL = scrapy.Field()

    WK = scrapy.Field()
    Game_Date = scrapy.Field()
    OPP = scrapy.Field()
    RESULT = scrapy.Field()
    REC = scrapy.Field()
    YDS = scrapy.Field()
    AVG = scrapy.Field()
    LNG = scrapy.Field()
    TD = scrapy.Field()
    ATT = scrapy.Field()
    YDS1 = scrapy.Field()
    AVG1 = scrapy.Field()
    LNG1 = scrapy.Field()
    TD1 = scrapy.Field()
    FUM = scrapy.Field()
    LOS = scrapy.Field()

