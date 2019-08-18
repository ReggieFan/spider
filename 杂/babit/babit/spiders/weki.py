# -*- coding: utf-8 -*-
import scrapy


class WekiSpider(scrapy.Spider):
    name = 'weki'
    allowed_domains = ['']
    start_urls = ['http:///']

    def parse(self, response):
        pass
