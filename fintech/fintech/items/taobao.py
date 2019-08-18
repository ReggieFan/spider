from scrapy import Field
from scrapy import Item

class TaobaoItem(Item):
    name = Field()
    price = Field()