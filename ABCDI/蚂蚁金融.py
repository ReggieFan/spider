import lxml
from lxml import html
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = requests.get('https://tech.antfin.com/search?query='+quote('区块链', 'utf-8')+'&type=all&size=10&from=0', headers=headers)
req.encoding = req.apparent_encoding
htm = lxml.html.fromstring(req.text)
# for i in htm.xpath('//script'):
#     print (i.text)
# print (unquote(htm.xpath('//script')[4].text))
for i in htm.xpath('//a'):
    print(i.text)
    print (i.get('href'))

req = request.Request('https://tech.antfin.com/search?query='+quote('区块链', 'utf-8')+'&type=all&size=10&from=0', headers=headers)
html = urlopen(req)
print (BeautifulSoup(html.read(), "html.parser").find_all('script'))




