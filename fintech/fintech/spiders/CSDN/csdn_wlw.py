# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

class CsdnWlwSpider(scrapy.Spider):
    name = 'csdn_wlw'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['http://blog.csdn.net/']

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        start=['物联网']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        req = request.Request('https://so.csdn.net/so/search/s.do?q='+quote(start[0], 'utf-8')+'&t=blog&o=&s=&l=', headers=headers)
        htm = urlopen(req)
        bsObj = BeautifulSoup(htm.read(), "html.parser")
        bs = bsObj.find(attrs={'class':'relation-search csdn-tracking-statistics'}).ul
        for i in bs.find_all('li'):
            try:
                start.append(i.text.replace('\n',''))
            except:
                pass
        num=1000
        for j in start:
            for i in range(1,1001):
                yield Request('https://so.csdn.net/so/search/s.do?p='+str(i)+
                              '&q='+quote(j, 'utf-8')+'&t=blog&domain=&o=&s=&u=&l=&f=&rbg=0',
                              self.parse)
                print('CSDN'+j+'：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'limit_width'})
        # print (bs[0].a.get('href'))
        # yield Request(bs[0].a.get('href'),self.parse_2,
        #                       meta={'url':bs[0].a.get('href')})
        for j in bs:
            yield Request(j.a.get('href'),self.parse_2,
                              meta={'url':j.a.get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'id': 'content_views'})
        content = bs.text
        # for i in bs.find_all('p'):
        #     content = f'{content}{i.text}'
        title = bsObj.find(attrs={'class': 'title-article'}).text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        item['abstract'] = content[:60]
        item['content'] = content
        item['vender'] = ''
        return item