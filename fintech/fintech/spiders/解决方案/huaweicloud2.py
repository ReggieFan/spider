# -*- coding: utf-8 -*-
#解决方案
import scrapy
from fintech.items.antfin import AntfinItem #这里不知道为什么报错，都是运行没问题
from scrapy.http import Request
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
        else:
            out_str=out_str+' '
    return out_str
def is_uchar(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    if uchar=='，':
        return True
    # """判断一个unicode是否是数字"""
    # if uchar >= u'\u0030' and uchar<=u'\u0039':
    #     return True
    return False

class HuaweicloudSpider2(scrapy.Spider):
    name = 'huaweicloud2'
    allowed_domains = ['huaweicloud.com']
    start_urls = ['http://huaweicloud.com/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        for j in range(22,23):
            for i in range(1,11):
                yield Request('https://www.huaweicloud.com/s/JeeJqeiBlOe9kSU/t_'+str(j)+
                              '_p_'+str(i),self.parse,headers=headers)

    def parse(self, response):
        bsObj = BeautifulSoup(response.text, "lxml")
        bs = bsObj.find_all(attrs={'class': 'search-txtw1'})
        # print (bs[0].a.get('href'))
        # yield Request(bs[0].a.get('href'),self.parse_2,
        #                       meta={'url':bs[0].a.get('href')})
        for j in bs:
            yield Request(j.a.get('href'),self.parse_2,
                              meta={'url':j.a.get('href')})

    def parse_2(self,response):
        # print('parse2')
        bsObj = BeautifulSoup(response.text, "lxml")
        # print (response.text)
        contain=['solution-trends-new-v5','solution-scene-v5','solution-framework-v5'
            ,'solution-trends-v5','solution-challenge-v5','solution-architecturel-v5',
                 'solution-advantage-v5','solution-service-v5']
        content = ''
        for i in contain:
            a = bsObj.find(attrs={'class':i})
            if a!=None:
                text=(is_ustr(a.text))
                content = f'{content}{text}'
        title = bsObj.find('h1').text.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
        content = content.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "").replace("\xa0", "").replace('\u3000','')
        # print ('标题：'+title+'内容：'+content)
        summary=bsObj.find(attrs={'class':'solution-banner-text'})
        if summary!=None:
            summary=summary.text.replace("\n", "").replace("\r", "").replace(" ", "").replace("\t", "")
        else:
            summary=content[:40]
        item = AntfinItem()
        item['type'] = 1
        item['url'] = response.meta['url']
        item['title'] = title
        item['summary'] = summary
        item['content'] = content
        item['vender'] = '华为云'
        return item