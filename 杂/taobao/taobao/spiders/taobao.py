# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

class ThirddemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    comment = scrapy.Field()
	print ('itemstart')
    pass
	
class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = ['http://taobao.com/']
	print('spiderstart')

    def parse(self, response):
        key = '小吃'
        for i in range(0, 2):
            url = 'https://s.taobao.com/search?q=' + str(key) + '&s=' + str(44*i)
            print(url)
            yield Request(url=url, callback=self.page)
        pass

    def page(self, response):
        body = response.body.decode('utf-8','ignore')
        pattam_id = '"nid":"(.*?)"'
        all_id = re.compile(pattam_id).findall(body)
        # print(all_id)
        for i in range(0, len(all_id)):
            this_id = all_id[i]
            url = 'https://item.taobao.com/item.htm?id=' + str(this_id)
            yield Request(url=url, callback=self.next)
            pass
        pass

    def next(self, response):
        # print(response.url)
        url = response.url
        pattam_url = 'https://(.*?).com'
        subdomain = re.compile(pattam_url).findall(url)
        # print(subdomain)
        if subdomain[0] != 'item.taobao':
            title = response.xpath("//div[@class='tb-detail-hd']/h1/text()").extract()
            pass
        else:
            title = response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
            pass
        self.num = self.num + 1;
        print(title)
        # 获取商品的id（用于构造商品评论数量的抓包网址）
        if subdomain[0] != 'item.taobao':  # 如果不属于淘宝子域名，执行if语句里面的代码
            pattam_id = 'id=(.*?)&'
            this_id = re.compile(pattam_id).findall(url)[0]
            pass
        else:
            # 这种情况是不能使用正则表达式的，正则表达式不能获取字符串最末端的字符串
            pattam_id = 'id=(.*?)$'
            this_id = re.compile(pattam_id).findall(url)[0]
            pass
        print(this_id)
        # 构造具有评论数量信息的包的网址
        comment_url = 'https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=' + str(this_id)

        # 这个获取网址源代码的代码永远也不会出现错误，因为这个URL的问题，就算URL是错误的，也可以获取到对应错误网址的源代码。
        # 所以不需要使用 try 和 except urllib.URLError as e 来包装。
        comment_data = urllib.request.urlopen(comment_url).read().decode('utf-8', 'ignore')
        pattam_comment = '"rateTotal":(.*?),"'
        comment = re.compile(pattam_comment).findall(comment_data)
        # print(comment)
        item['comment'] = comment
        yield item

class taobaoPipeline(object):
    def process_item(self, item, spider):
        title = item['title'][0]
        link = item['link']
        price = item['price'][0]
        comment = item['comment'][0]
        print('商品名字', title)
        print('商品链接', link)
        print('商品正常价格', price)
        print('商品评论数量', comment)
        print('------------------------------\n')
        return item
        pass
