# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from bs4 import BeautifulSoup

class LeadaiMlSpider(scrapy.Spider):
    name = 'leadai_ml'
    allowed_domains = ['leadai.org']
    start_urls = ['http://leadai.org/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        num=23
        for i in range(1,num):
            yield Request('http://www.leadai.org/yuyanchuli/list_3_'+str(i)+'.html',
                          self.parse)
            print('LeadNLP：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all('h3')
        for j in bs:
            yield Request('http://www.leadai.org'+j.a.get('href'),self.parse_2,
                              meta={'url':'http://www.leadai.org'+j.a.get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        bs = bsObj.find(attrs={'class': 'article-content'})
        content=bs.text
        # for i in bs.find_all('p')[:-2]:
        #     content = f'{content}{i.text}'
        title = bsObj.find('h3').text
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

