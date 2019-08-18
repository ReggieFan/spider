# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com']
    start_urls = ['http://techcrunch.com/']

    def start_requests(self):
        # s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # pattern = re.compile('article*')
        for i in range(1, 2):
            data = {'yhlVer': 2,
                    'yhlClient': 'rapid',
                    'yhlS': 1197802919,
                    'yhlCT': 2,
                    'yhlBTMS': 1556423813660,
                    'yhlClientVer': '3.53.5',
                    'yhlRnd': 'mADSkJrtPwGRjVN8',
                    'yhlCompressed': 0}
            ajax = requests.post('https://udc.yahoo.com/v2/public/yql?',
                         data=data, headers=headers)
            total = ajax.text
            print (total)
            # print (total['loadMore']['html'])
    #         bsObj = BeautifulSoup(total['loadMore']['html'], "lxml")
    #         bs=bsObj.find_all(attrs={'class':'thumb'})
    #         for j in bs:
    #             # print(j.get('href'))
    #             # print (j)
    #             yield Request('https://www.zdnet.com'+j.get('href'),self.parse,
    #                               meta={'url':'https://www.zdnet.com'+j.get('href')})
    #         print('zdnet：' + '%.2f' % ((i-1) /1000  * 100) + "%")
    # #
    # def parse(self, response):
    #     bsObj = BeautifulSoup(response.text, "lxml")
    #     bs = bsObj.find(attrs={'class': 'storyBody'})
    #     content = bs.text
    #     title = bsObj.find(['h1']).text
    #     content = content.replace("\n", "").replace("\r", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
    #     item = AntfinItem()
    #     item['type'] = 2
    #     item['url'] = response.meta['url']
    #     item['title'] = title
    #     item['summary'] = content[:60]
    #     item['content'] = content
    #     item['vender'] = ''
    #     return item