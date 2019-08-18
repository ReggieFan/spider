# -*- coding: utf-8 -*-
import scrapy
from ..items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from urllib.parse import quote
from lxml import etree
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
#这个一运行内存就满不知道为啥
class Yjs360Spider(scrapy.Spider):
    name = 'yjs360'
    allowed_domains = ['btime.com']
    start_urls = ['http://btime.com/']


    def parse(self, response):  # 这个很奇怪，一定要写parse
        items = []
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        print(response.text)
        driver = webdriver.Chrome()
        driver.get('https://www.btime.com/search?q=' + quote('云计算', 'utf-8'))
        for i in range(4000):
            print('获取url:' + '%.2f' % (i / 4000) + '%')
            for i in range(5):
                driver.execute_script("var q=document.documentElement.scrollTop=100000")
                time.sleep(1)
            try:
                driver.find_element_by_class_name('icon-more-feed').click()
            except:
                pass
        req = driver.page_source
        htm = etree.HTML(req)
        href = []
        for i in htm.xpath('// *[ @ class = "feed-lp-rt"]'):
            print(i.get('href'))
            href.append(i.get('href'))

        count = 0
        num = len(href)
        for url in href:
            try:
                print('360云计算' + '%.2f' % (count / num * 100) + "%")
                count += 1
                req = request.Request(url, headers=headers)
                html = urlopen(req)
                bsObj = BeautifulSoup(html.read(), "html.parser")
                bs = bsObj.find_all(['p'])
                #         print(bsObj.find(['title']).text)
                content = ''
                for i in bs:
                    if i.text != '' and i.text not in content:
                        # content = f'{content}{i.text}'
                        content =content.join(i.text)
                content=content.replace("\n", "").replace("\r", "")
                # print(content)
                item = AntfinItem()
                item['type'] = 2
                item['url'] = url
                item['title'] = bsObj.find(['title']).text.replace('\n','').replace("\r", "").replace(" ", "")
                item['abstract'] = content[:40]
                item['content'] = content
                item['vender'] = ''
                return item
            except:
                pass
        # return items
