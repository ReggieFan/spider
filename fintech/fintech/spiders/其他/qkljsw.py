# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from bs4 import BeautifulSoup

class QkljswSpider(scrapy.Spider):
    name = 'qkljsw'
    allowed_domains = ['qkljsw.com']
    start_urls = ['http://qkljsw.com/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        num=76
        for i in range(1,num):
            yield Request('http://qkljsw.com/posts/page/'+str(i),
                          self.parse)
            print('区块链技术网：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all('h2')
        # print (bs)
        for j in bs:
            yield Request(j.find('a').get('href'),self.parse_2,
                              meta={'url':j.find('a').get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class': 'content_post'})
        content=''
        for i in bs.find_all('p')[:-1]:
            content = f'{content}{i.text}'
        title = bsObj.find('h1').text
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