# -*- coding: utf-8 -*-
import scrapy
import requests
import json,re
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.parse import quote

class A360YjsSpider(scrapy.Spider):
    name = '360_yjs'
    allowed_domains = ['btime.com']
    start_urls = ['http://btime.com/']

    def start_requests(self):
        s = requests.session()
        # 'Accept - Encoding':'gzip, deflate, sdch',
        # 'Accept - Language': 'zh - CN, zh;q = 0.8',
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        headers = {'Accept': '* / *',
        'Connection': 'keep - alive',
        'Cookie': 'usid=16703f43ce20ba51fb6ed44bf9bd4a61; __guid=899382f8-5167-11e9-9a0d-6c92bf418e4a; __DC_gid=196757375.883154844.1553784071761.1554640243267.42',
        'Host': 'pc.api.btime.com',
        'Referer': 'https://www.btime.com/search?src=tab_web&q=%E5%8C%BA%E5%9D%97%E9%93%BE',
        'User - Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        # pattern = re.compile('article*')
        for i in range(1, 10000):
            data = {'callback': 'jQuery111308174540904420109_1554126378136',
                    'q': '云计算',
                    'type': 'all',
                    'channel': 'search',
                    'device_id': '439b109dde59c61891c1418ad0d32e4c',
                    'refresh': 6,
                    'req_count': i,
                    'refresh_type': 2,
                    'pid': 3}
            ajax = s.get('https://pc.api.btime.com/btimeweb/getSearchData?',
                         params=data, headers=headers)
            total = json.loads(ajax.text[ajax.text.find('{'):-1])
            for j in total['data']:
                yield Request(j['open_url'],self.parse,
                                  meta={'url':j['open_url']})
            print('360云计算：' + '%.2f' % ((i-1) /10000  * 100) + "%")

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(['p'])
        #         print(bsObj.find(['title']).text)
        content = ''
        for i in bs:
            if i.text != '' and i.text not in content:
                content = f'{content}{i.text}'
        title=bsObj.find(['h1']).text
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