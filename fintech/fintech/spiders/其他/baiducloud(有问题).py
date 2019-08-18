# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import quote
from bs4 import BeautifulSoup
from fintech.items.antfin import AntfinItem

class BaiducloudSpider(scrapy.Spider):
    name = 'baiducloud'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def start_requests(self):
        start={'云计算':202,'物联网':70,'大数据':598,'区块链':6,'人工智能':203}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        for j in start:
            num=start[j]
            for i in range(1,2):
                yield Request('https://cloud.baidu.com/search.html?q='+
                              quote(j, 'utf-8')+'&type=doc&pn='+str(i),
                              self.parse,headers=headers)
                print('Baiducloud'+j+'：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        # bs = bsObj.find_all(attrs={'class': 'title'})
        # print (bs[0].a.get('href'))
        # yield Request(bs[0].a.get('href'),self.parse_2,
        #                       meta={'url':bs[0].a.get('href')})
        bs = bsObj.find(attrs={'id': 'result-main'})
        print (bs.text)
        # for j in bs:
        #     print (j.text)
    #     for j in bs:
    #         yield Request(j.a.get('href'),self.parse_2,
    #                           meta={'url':j.a.get('href')})
    #
    # def parse_2(self,response):
    #     # print('parse2')
    #     bsObj = BeautifulSoup(response.text, "lxml")
    #     # print (response.text)
    #     bs = bsObj.find(attrs={'class': 'markdown-body'})
    #     content = ''
    #     for i in bs.find_all(['p','h2','h3','li']):
    #         content = f'{content}{i.text}'
    #     title = bsObj.find('h1').text
    #     content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
    #     # print ('标题：'+title+'内容：'+content)
    #     item = AntfinItem()
    #     item['type'] = 2
    #     item['url'] = response.meta['url']
    #     item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
    #     item['abstract'] = content[:60]
    #     item['content'] = content
    #     item['vender'] = ''
    #     return item
