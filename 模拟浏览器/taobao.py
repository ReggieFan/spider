import lxml
from lxml import etree
import requests
import time
import re,csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import request
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()
pattern = re.compile('/article*')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# driver.get('https://s.taobao.com/search?q=书包&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306')
# driver.execute_script("var q=document.documentElement.scrollTop=100000")

s = requests.session()
html=s.get('https://s.taobao.com/search?q=书包&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306',headers=headers)
print(html.text)
# time.sleep(2)
# for i in range(10):
#     print ('第'+str(numb+1)+'部分:'+'获取url:'+'%.2f'%(i/4000)+'%')
#     try:
#         driver.find_element_by_xpath('// *[ @ id = "news"] / div[2] / a').click()
#     except:
#         pass
#     driver.execute_script("var q=document.documentElement.scrollTop=100000")
req=driver.page_source
htm = etree.HTML(req)

# href=[]
# for i in htm.xpath('//a'):
#     if re.match(pattern, i.get('href')):
#         if i.get('href') in href:
#             continue
#         href.append(i.get('href'))
# print (href)
# try :
#     leng=len(href)
#     count=0
#     # print('try')
#     for k in href:
#         print('第'+str(numb+1)+'部分:'+'爬取数据'+'%.2f' % (count/leng*100)+'%')
#         count+=1
#         req = request.Request('https://www.8btc.com' + k, headers=headers)
#         html = urlopen(req)
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         bs = bsObj.find_all(['h2', 'p'])
#         # print(bsObj.find(['title']).text)
#         content=''
#         for j in bs:
#             content = f'{content}{j.text}'
#         content.replace("\n", "").replace("\r", "")
#     # print(content)
#         csv_writer.writerow((2,k, bsObj.find(['title']).text,content[:40],
#                              content, ''))
# except:
#     pass




