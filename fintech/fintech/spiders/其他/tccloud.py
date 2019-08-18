# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class TccloudSpider(scrapy.Spider):
    name = 'tccloud'
    allowed_domains = ['tencent.com']
    start_urls = ['http://tencent.com/']

    def start_requests(self):
        s = requests.session()
        'https://cloud.tencent.com/developer/services/ajax/search?action=SearchList'
        headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        # pattern = re.compile('article*')
        for i in range(1, 10):
            data = {'action': "SearchList", 'payload': {'pageNumber': 2, 'q': "云计算", 'searchTab': "article"}}
            ajax = s.post('https://cloud.tencent.com/developer/services/ajax/search?action=SearchList', data=data, headers=headers)
            print (ajax.text)
    #         total = json.loads(ajax.text[ajax.text.find('{'):-1])
    #         for j in total['data']:
    #             yield Request(j['open_url'],self.parse,
    #                               meta={'url':j['open_url']})
    #         print('360云计算：' + '%.2f' % ((i-1) /10000  * 100) + "%")
    #
    # def parse(self, response):
    #     bsObj = BeautifulSoup(response.text, "lxml")
    #     bs = bsObj.find_all(['p'])
    #     #         print(bsObj.find(['title']).text)
    #     content = ''
    #     for i in bs:
    #         if i.text != '' and i.text not in content:
    #             content = f'{content}{i.text}'
    #     title=bsObj.find(['h1']).text
    #     content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
    #     # print ('标题：'+title+'内容：'+content)
    #     item = AntfinItem()
    #     item['type'] = 2
    #     item['url'] = response.meta['url']
    #     item['title'] = title
    #     item['abstract'] = content[:60]
    #     item['content'] = content
    #     item['vender'] = ''
    #     return item