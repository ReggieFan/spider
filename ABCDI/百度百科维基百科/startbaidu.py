
import csv
from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen
import lxml
from lxml import html
from urllib.parse import quote
import requests
def search(s):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    req = request.Request('https://baike.baidu.com/item/'+quote(s, 'utf-8'), headers=headers)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    bs=bsObj.find_all(name='div',attrs={'class':'para'})
    content=""
    for i in bs:
        content=f'{content}{i.text}'
    return content

def get_relevant_keys(key):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = requests.get('https://baike.baidu.com/item/'+quote(key, 'utf-8'), headers=headers)
    req.encoding = req.apparent_encoding
    htm = lxml.html.fromstring(req.text)
    html_data = htm.xpath('//*[@class="para"]/a')
    keys=[]
    for i in html_data:
        if (i.text!='\xa0'and i.text!=None):
            keys.append(i.text)
    return keys

fintech=['区块链','人工智能','云计算','大数据','物联网']
for name in fintech:
    totalkeys=[]
    for i in range(3):
        totalkeys.extend(get_relevant_keys(name))
    totalkeys = list(set(totalkeys))
    totalkeys2 = totalkeys.copy()
    for i in totalkeys:
        totalkeys2.extend(get_relevant_keys(i))
        # print (i)
    totalkeys2 = list(set(totalkeys2))
    length=len(totalkeys2)
    print(length,totalkeys2)
    count=0
    with open('d://'+name+'.csv', 'w', newline='',encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('title','abstract','type','content'))
        for i in totalkeys2:
            print((name+'%.2f'%(count/length*100)) + "%")
            count+=1
            try :
                content = search(i)
                content.replace("\n", "").replace("\r", "")
                csv_writer.writerow((i, content[:20], name, content))
            except:
                pass

