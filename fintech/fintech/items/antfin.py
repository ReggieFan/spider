from scrapy import Field
from scrapy import Item

class AntfinItem(Item):
    title = Field()
    summary = Field()
    type = Field()
    content = Field()
    url= Field()
    vendor= Field()