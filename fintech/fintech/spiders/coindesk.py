# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class CoindeskSpider(scrapy.Spider):
    name = 'coindesk'
    allowed_domains = ['coindesk.com']
    start_urls = ['http://coindesk.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        # pattern = re.compile('article*')
        for i in range(1,132):
            ajax = s.get('https://www.coindesk.com/wp-json/v1/category/7253/'+str(i), headers=headers)
            total = json.loads(ajax.text)
            bsObj = BeautifulSoup(total['stream'], "lxml")
            # print(bsObj)
            bs = bsObj.find(attrs={'class':'article-set'})
            for j in bs.find_all('a'):
                # print(i.get('href'))
            # for j in total['data']:
                if 'coin' in j.get('href'):
                    yield Request(j.get('href'),self.parse,
                                      meta={'url':j.get('href')})
            print('coindesk：'+str(((i-1)/132*100))+"%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find(attrs={'class':'entry-content'})
        content = ''
        for i in bs.text:
            content = f'{content}{i}'
        title=bsObj.find(['h1']).text
        content = content.replace("\n", "").replace("\r", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title
        item['summary'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item
