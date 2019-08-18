# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class YjsZjmdmSpider(scrapy.Spider):
    name = 'yjs_zjmdm'
    allowed_domains = ['searchcloudcomputing.techtarget.com.cn']
    start_urls = ['http://searchcloudcomputing.techtarget.com.cn/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        # count=0
        num=48
        for i in range(2,num):
            yield Request('https://searchcloudcomputing.techtarget.com.cn/interviews/page/'+str(i),
                          self.parse,headers=self.headers)
            print('TechTarget专家面对面：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'newslist'})
        for j in bs:
            for k in j.find_all('h4'):
                yield Request(k.find('a').get('href'),self.parse_2,
                              meta={'url':k.find('a').get('href')},headers=self.headers)

    def parse_2(self,response):
        bsObj = BeautifulSoup(response.text, "lxml")
        ma = bsObj.find(attrs={'class': 'maintext'})
        bs = ma.find_all('p')
        content = ''
        for i in bs:
            content = f'{content}{i.text}'
        title = bsObj.find(attrs={'class': 'sctopbannercon'}).h1.text
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
        # print ('标题：'+title+'内容：'+content)
        item = AntfinItem()
        item['type'] = 2
        item['url'] = response.meta['url']
        item['title'] = title.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
        item['summary'] = content[:40]
        item['content'] = content
        item['vendor'] = ''
        return item
