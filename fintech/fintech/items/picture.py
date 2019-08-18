from scrapy import Field
from scrapy import Item


class CrawlpicturesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # url = Field()
    keyword=Field()
    image_name = Field()
    image_urls = Field()
