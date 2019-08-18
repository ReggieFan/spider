# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class JznDlSpider(scrapy.Spider):
    name = 'jzn_dl'
    allowed_domains = ['ziiai.com']
    start_urls = ['http://ziiai.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        # pattern = re.compile('article*')
        for j in range(1, 4):
            data = {'page': j,'res_type': 'html','type': 'dl','topic_id': 329}
            ajax = s.get('https://www.ziiai.com/api/home/articles?', params=data, headers=headers)
            total = json.loads(ajax.text)
            # print (total['result'])
            bsObj = BeautifulSoup(total['result'][0], "lxml")
            bs = bsObj.find_all('a')
            # text = re.compile(r".*[0-9]$")
            href = []
            for i in bs:
                # if text.match(i.get('href')):
                href.append(i.get('href'))
            print (set(href))
            for i in set(href):
                yield Request(i,self.parse,meta={'url':i})
            print('极智能：' + '%.2f' % ((j-1) /4  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class':'article-detail p16'})
        # print(bs)
        bs=bs.find_all('p')
        # print(bsObj.find(['title']).text)
        content = ''
        for j in bs:
            content = f'{content}{j.text}'
        title = bsObj.find(['h1']).text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0","").replace('\u3000', '')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title
        item['abstract'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item