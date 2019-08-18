# -*- coding: utf-8 -*-
import scrapy
from ..items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from urllib.parse import quote
from lxml import etree
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy.http import Request

#这个一运行内存就满不知道为啥
class Dsj360Spider(scrapy.Spider):
    name = 'dsj360'
    allowed_domains = ['btime.com']
    start_urls = ['http://btime.com/']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # print(response.text)
    driver = webdriver.Chrome()
    driver.get('https://www.btime.com/search?q=' + quote('大数据', 'utf-8'))
    for i in range(5):
        print('获取url:' + '%.2f' % (i / 4000 * 100) + '%')
        for i in range(5):
            driver.execute_script("var q=document.documentElement.scrollTop=100000")
            time.sleep(0.5)
        try:
            driver.find_element_by_class_name('icon-more-feed').click()
        except:
            pass
        driver.execute_script("var q=document.documentElement.scrollTop=100000")
    req = driver.page_source
    htm = etree.HTML(req)
    href = []
    for i in htm.xpath('// *[ @ class = "feed-lp-rt"]'):
        print(i.get('href'))
        href.append(i.get('href'))
    items=[]
    num=len(href)
    tcount=0

    def start_requests(self):
        # href=['http://www.baidu.com','http://www.taobao.com']
        count=0
        for url in self.href:
            yield Request(url, self.parse, meta={'url':url})
            print('360大数据' + '%.2f' % (count / self.num * 100) + "%")
            count += 1

    def parse(self, response):
        item = AntfinItem()
        self.tcount+=1
        try:
            bsObj = BeautifulSoup(response.text, "lxml")
            bs = bsObj.find_all(['p'])
            #         print(bsObj.find(['title']).text)
            content = ''
            for i in bs:
                if i.text != '' and i.text not in content:
                    content = content.join(i.text)
            content = content.replace("\n", "").replace("\r", "")
            # print(content)
            item['type'] = 2
            item['url'] = response.meta['url']
            item['title'] = bsObj.find(['title']).text.replace('\n', '').replace("\r", "").replace(" ", "")
            item['abstract'] = content[:40]
            item['content'] = content
            item['vender'] = ''
            return item
            # time.sleep(0.5)
        except:
            pass