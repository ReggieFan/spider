# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class ZdnetSpider(scrapy.Spider):
    name = 'zdnet'
    allowed_domains = ['zdnet.com']
    start_urls = ['http://zdnet.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for i in range(1, 1000):
            data = {'endpoint': '/api/component/listing/40df48a6-2074-40bf-9854-18faaf9cb39f/content/68eacfec-1908-4292-97b0-5a8928e7c258',
                    'view': 'river',
                    'familyName': 'listing',
                    'typeName': 'multi_filtered_listing',
                    'offset': i*15,
                    'initialLimit': 0,
                    'limit': 15,
                    'lastAssetId': 'e0324ff9-bc26-4624-a137-40682580a618'}
            ajax = s.get('https://www.zdnet.com/components/load-more/xhr/?',
                         params=data, headers=headers)
            total = json.loads(ajax.text)
            # print (total['loadMore']['html'])
            bsObj = BeautifulSoup(total['loadMore']['html'], "lxml")
            bs=bsObj.find_all(attrs={'class':'thumb'})
            for j in bs:
                # print(j.get('href'))
                # print (j)
                yield Request('https://www.zdnet.com'+j.get('href'),self.parse,
                                  meta={'url':'https://www.zdnet.com'+j.get('href')})
            print('zdnet：' + '%.2f' % ((i-1) /1000  * 100) + "%")
    #
    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find(attrs={'class': 'storyBody'})
        content = bs.text
        title = bsObj.find(['h1']).text
        content = content.replace("\n", "").replace("\r", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title
        item['summary'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item