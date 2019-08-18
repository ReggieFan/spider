# -*- coding: utf-8 -*-
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from bs4 import BeautifulSoup


class SharpcloudSpider(scrapy.Spider):
    name = 'sharpcloud'
    allowed_domains = ['sharpcloud.cn']
    start_urls = ['http://sharpcloud.cn/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        num=90
        for i in range(1,num+1):
            yield Request('http://www.sharpcloud.cn/cloud/index.php?page='+str(i),
                          self.parse, headers=headers)
            print('锋云：' + '%.2f' % ((i-1) /num  * 100) + "%")

    def parse(self, response):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
            ,'Host': 'www.sharpcloud.cn'
            ,'Cookie': 'discuz_2132_saltkey=iuMsp0Et; discuz_2132_lastvisit=1554979443; bdshare_firstime=1554983033752; discuz_2132_sid=VhxjyY; discuz_2132_sendmail=1; Hm_lvt_5296c00c3a81b19f5ed6d2cf915c8177=1554983034,1555124340,1555413360; Hm_lpvt_5296c00c3a81b19f5ed6d2cf915c8177=1555413360; discuz_2132_lastact=1555413372%09misc.php%09secqaa; discuz_2132_secqaa=79.ce6d21aa881a95d91a'
            ,'_dsign':'664e3385'}
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'xs2'})
        for j in bs:
            # print (j)
            if j.find('a')!=None:
                yield Request(j.find('a').get('href'),self.parse_2,
                              meta={'url':j.find('a').get('href')},headers=headers)

    def parse_2(self,response):
        print (response.meta['url'])
        # print('parse2')
        print(response.text)
    #     bsObj = BeautifulSoup(response.text, "lxml")
    #     # print (response.text)
    #     title = bsObj.find('h1').text
    #     print (title)
    #     bs = bsObj.find_all(attrs={'id': 'ct'})
    #     print(bs)
        # content = bs.text
        # # for i in bs.find_all('p'):
        # #     content = f'{content}{i.text}'

        # content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # # print ('标题：'+title+'内容：'+content)
        # item = AntfinItem()
        # item['type'] = 2
        # item['url'] = response.meta['url']
        # item['title'] = title.replace('\n', '').replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # item['abstract'] = content[:60]
        # item['content'] = content
        # item['vender'] = ''
        # return item