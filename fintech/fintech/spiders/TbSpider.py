# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
from ..items.taobao import TaobaoItem
import re
import urllib.robotparser


class TbSpider(scrapy.Spider):
    name = "TbSpider"
    allowed_domains = ["taobao.com"]
    start_urls = ['https://taobao.com/']

    def parse(self, response):
        headers = {
            'authority': 's.taobao.com',
            'method': 'GET',
            'path': '/search?q=%E4%B9%A6%E5%8C%85&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, sdch',
            'accept-language': 'zh-CN,zh;q=0.8',
            'cache-control': 'max-age=0',
            'cookie': 'miid=770433044453625467; thw=cn; cna=BJJEE9dz4WICAd7Jrd5cAkZh; tracknick=onion66591813; tg=0; t=2d5ea67b67d706cbe4e7a4496c6074c1; lgc=onion66591813; enc=bQxtPDBUEm9I5vAndnQUxhPAs6TgPkcoSLgm3HFuogIm8xPsr9FUttCbX57g5RDH6g4FiOg88spIBEZjC7i3UA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=35_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc3=nk2=DN9io9s1hTRzh86xkg%3D%3D&vt3=F8dBy32ghvdeqP3L9KM%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUGrfolO4Dxs7g%3D%3D; uc4=nk4=0%40DsiGbdHMyUymq%2Fc7U83mpiiFVgcvfAwr&id4=0%40U2OcTk%2BbAq5VXB7CuMB5IOSYSuVS; _cc_=WqG3DMC9EA%3D%3D; _uab_collina=156509429964604588130004; x5sec=7b227365617263686170703b32223a226235376635343366366439643331643766366631636539616531363730386237434d506a70656f46455072382f386d65785033594e686f4d4d6a6b354f44417a4d7a63774e7a7378227d; JSESSIONID=CA3FCC6BECFE8AF60B71851D5804EF49; isg=BLi4170LEVJfvHwWbgkkSsDEiWaU6K_77RkgFPIpBPOmDVj3mjHsO84vwUUYRtSD; l=cBTeLAD4vXsFWdz9BOCanurza77OSIRYYuPzaNbMi_5dq6T_BtbOk5gTwF96VjWd95YB4Hz2mJp9-etkqylFDj--g3fP.; swfstore=305404',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        for i in range(1):
            url = 'https://s.taobao.com/search?q=nike&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190806&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=' + str(i * 44)
            # r = requests.get(url, timeout=30, headers=headers)
            yield Request(url=url, callback=self.page2, headers=headers)
        # print(r.text)

    def page2(self,response):
        # response.raise_for_status()
        # response.encoding = response.apparent_encoding
        # print(r.text)
        html = response.text
        # print (html)
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        print(plt, tlt)
        for i in range(len(plt)):
            try:
                price = eval(plt[i].split(':')[1])   #eval可以去掉最外层的引号
                title = eval(tlt[i].split(':')[1])
                item = TaobaoItem()
                item['price'] = price
                item['name'] = title
                yield item
                # yield Request(callback=self.page3,url='https://taobao.com/',meta={'price':price,'title':title})
            except:
                print('转化price，title出现问题')

