# -*- coding: utf-8 -*-
import scrapy,selenium
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

class BaikeSpider(scrapy.Spider):
	name = 'baike'

	def parse(self):
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
		req = request.Request('https://baike.baidu.com/item/'+quote('区块链', 'utf-8'), headers=headers)
		html = urlopen(req)
		bsObj = BeautifulSoup(html.read(), "html.parser")
		bs=bsObj.find_all(name='div',attrs={'class':'para'})
		items=[]
		for i in bs:
			item = BaiduItem()
			print (i.text)
			item['title']="区块链"
			item['abstract']=i.text[:30]
			item['type']="文档"
			item['content']=i.text
			items.append(item)
		return items
			
