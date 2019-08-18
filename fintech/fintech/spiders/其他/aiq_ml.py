# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from urllib.parse import quote
from bs4 import BeautifulSoup

class AiqMlSpider(scrapy.Spider):
    name = 'aiq_ml'
    allowed_domains = ['6aiq.com']
    start_urls = ['http://6aiq.com/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        num=40
        for i in range(1,41):
            yield Request('http://www.6aiq.com/domain/machine_learning?p='+str(i),
                          self.parse,headers=headers)
            print('AIQ机器学习：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find(attrs={'class': 'article-list list'})
        for j in bs.find_all('h2'):
            yield Request(j.a.get('href'),self.parse_2,
                              meta={'url':j.a.get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class': 'content-reset article-content'})
        content=''
        for i in bs.find_all('p')[:-2]:
            content = f'{content}{i.text}'
        title = bsObj.find(attrs={'class':'article-title'}).text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        item['summary'] = content[:60]
        item['content'] = content
        item['vendor'] = ''
        return item