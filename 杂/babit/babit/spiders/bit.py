# -*- coding: utf-8 -*-
import scrapy
from ..antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from lxml import etree
import time
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

class BitSpider(scrapy.Spider):
    name = 'bit'
    allowed_domains = ['8btc.com']
    start_urls = ['https://www.8btc.com/news']


    def parse(self, response):  #这个很奇怪，一定要写parse
        items = []
        total = ['', '?cat_id=6168', '?cat_id=6167', '?cat_id=1647', '?cat_id=572', '?cat_id=242'
            , '?cat_id=6', '?cat_id=2963', '?cat_id=1799', '?cat_id=898']
        # total=['?cat_id=6168']
        pattern = re.compile('/article*')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # print('parse')
        # print (response.text)
        driver = webdriver.Chrome()
        for numb, name in enumerate(total):
            driver.get('https://www.8btc.com/news' + name)
            for i in range(1000):
                driver.execute_script("var q=document.documentElement.scrollTop=100000")
                time.sleep(2)
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
            count = 0
                # print('try')
            for k in href:
                try:
                    print('第' + str(numb + 1) + '部分:' + '爬取数据' + '%.2f' % (count / leng * 100) + '%')
                    count += 1
                    req = request.Request('https://www.8btc.com' + k, headers=headers)
                    html = urlopen(req)
                    bsObj = BeautifulSoup(html.read(), "html.parser")
                    bs = bsObj.find_all(['h2', 'p'])
                    # print(bsObj.find(['title']).text)
                    content = ''
                    for j in bs:
                        content = content.join(j.text)
                    content=content.replace("\n", "").replace("\r", "").replace(' ','')
                    # print(content)
                    item=AntfinItem()
                    item['type']=2
                    item['url']=k
                    item['title']=bsObj.find(['title']).text.replace('\n','').replace("\r", "").replace(" ", "")
                    item['abstract']=content[:40]
                    item['content']=content
                    item['vender']=''
                    items.append(item)
                except:
                    pass
        return items

