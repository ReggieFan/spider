# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request

class ChongdongSpider(scrapy.Spider):
    name = 'chongdong'
    allowed_domains = ['chongdongshequ.com']
    start_urls = ['http://chongdongshequ.com/']

    def start_requests(self):
        s = requests.session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        # pattern = re.compile('article*')
        for j in range(1, 75):
            ajax = s.get('https://www.chongdongshequ.com/api/article/hot/10000?format=html&page='+str(j),headers=headers)
            total = json.loads(ajax.text)
            # print (total['result'])
            bsObj = BeautifulSoup(total['html'], "lxml")
            bs = bsObj.find_all('a')
            # text = re.compile(r".*[0-9]$")
            href = []
            for i in bs:
                if 'article' in i.get('href') and 'comment' not in i.get('href'):
                    href.append(i.get('href'))
            print (set(href))
            for i in set(href):
                yield Request('https://www.chongdongshequ.com'+i,self.parse,meta={'url':'https://www.chongdongshequ.com'+i},headers=headers)
            print('虫洞-区块链：' + '%.2f' % ((j-1) /75  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        # print('parse')
        # print (bsObj)
        bs = bsObj.find(attrs={'class':'article-content'})
        content = bs.text
        bs = bsObj.find(attrs={'class': 'article-page'})
        title = bs.find('h1').text
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