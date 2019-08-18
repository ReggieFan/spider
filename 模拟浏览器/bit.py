# -*- coding: utf-8 -*-
import scrapy
from ..items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
import re
from lxml import etree
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy.http import Request

#这个一运行内存就满不知道为啥
class BitSpider(scrapy.Spider):
    name = 'bit'
    allowed_domains = ['8btc.com']
    start_urls = ['https://www.8btc.com/news']
    count=0

    def start_requests(self):  #这个很奇怪，一定要写parse
        # items = []
        # total = ['', '?cat_id=6168', '?cat_id=6167', '?cat_id=1647', '?cat_id=572', '?cat_id=242'
        #     , '?cat_id=6', '?cat_id=2963', '?cat_id=1799', '?cat_id=898']
        total=['?cat_id=6168']
        pattern = re.compile('/article*')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # print('parse')
        # print (response.text)
        driver = webdriver.Chrome()
        for numb, name in enumerate(total):
            driver.get('https://www.8btc.com/news' + name)
            for i in range(3):
                driver.execute_script("var q=document.documentElement.scrollTop=100000")
                time.sleep(1)
            for i in range(10):
                print('第' + str(numb + 1) + '部分:' + '获取url:' + '%.2f' % (i / 4000) + '%')
                try:
                    driver.find_element_by_xpath('// *[ @ id = "news"] / div[2] / a').click()
                except:
                    pass
                driver.execute_script("var q=document.documentElement.scrollTop=100000")
            req = driver.page_source
            htm = etree.HTML(req)
            print(name)
            href = []
            for i in htm.xpath('//a'):
                if re.match(pattern, i.get('href')):
                    if i.get('href') in href:
                        continue
                    href.append(i.get('href'))
            print(href)
            leng = len(href)
            # count = 0
            # print('try')
            for k in href:
                yield Request('https://www.8btc.com' + k,
                              self.parse, meta={'url': 'https://www.8btc.com' + k,
                                                'part':numb,'leng':leng})
            self.count=0
                # print('360大数据' + '%.2f' % (count / self.num * 100) + "%")


    def parse(self, response):
        print('第' + str(response.meta['part'] + 1) + '部分:' + '爬取数据'
              + '%.2f' % (self.count / response.meta['leng'] * 100) + '%')
        self.count += 1
        print ('第'+str(self.count)+'条数据')
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(['h2', 'p'])
        # print(bsObj.find(['title']).text)
        content = ''
        for j in bs:
            content = content.join(j.text)
        content=content.replace("\n", "").replace("\r", "").replace(' ','')
        # print(content)
        item=AntfinItem()
        item['type']=2
        item['url']=response.meta['url']
        item['title']=bsObj.find(['title']).text.replace('\n','').replace("\r", "").replace(" ", "")
        item['abstract']=content[:40]
        item['content']=content
        item['vender']=''
        return item

        # return items

