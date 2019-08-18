# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote

class BaidunewsSpider(scrapy.Spider):
    name = 'baidunews'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        num=1000
        for i in range(1,1001):
            yield Request('https://www.baidu.com/s?tn=news&word='+
                          quote('区块链','utf-8')+'&tngroupname=organic_news&pn='
                          +str(i*10),self.parse)
            print('百度资讯：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        print (response.text)
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'c-title'})
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
        bs = bsObj.find(attrs={'id': 'article-content'})
        content = ''
        for i in bs.find_all('p')[1:]:
            content = f'{content}{i.text}'
        title = bsObj.find(attrs={'class': 'article-title'}).text
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