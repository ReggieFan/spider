import lxml
from lxml import html
import requests
import csv
#获取：经营现金流/营业收入，销售现金流/营业收入，销售毛利率，资产增长率
name={'恒天海龙':'000677.SZ','吉林化纤':'000420.SZ','荣盛石化':'002493.SZ','金牛化工':'600722.SH','百傲化学':'603360.SH',
'沃华药业':'002107.SZ','联泰环保':'603797.SH','东江环保':'002672.SZ','昭衍新药':'603127.SH',
'驰宏锌锘':'600497.SH','开尔新材':'300234.SZ','ST康得新':'002450.SZ','ST狮头':'600539.SH'}

def stock1(code):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = requests.get('https://www.yiqiniu.com/gupiao/'+code+'/ZYZB', headers=headers)
    req.encoding = req.apparent_encoding
    htm = lxml.html.fromstring(req.text)
    x1 = htm.xpath('/html/body/div/div/div/div/div[3]/div/div/table[3]/tbody/tr[8]/td[5]')[0].text
    x2 = htm.xpath('/html/body/div/div/div/div/div[3]/div/div/table[3]/tbody/tr[7]/td[5]')[0].text
    x3 = htm.xpath('/ html / body / div / div / div / div / div[3] / div / div / table[3] / tbody / tr[4] / td[5]')[0].text
    return [x1,x2,x3]

def stock2(code):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = requests.get('https://www.yiqiniu.com/gupiao/'+code+'/ZCFZB', headers=headers)
    req.encoding = req.apparent_encoding
    htm = lxml.html.fromstring(req.text)
    for i in range(2,20):
        if (htm.xpath('/html/body/div/div/div/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td[1]')[0].text=='资产总计'):
            a = float(htm.xpath('/html/body/div/div/div/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td[5]')[0].text[:-1])
            b = float(htm.xpath('/html/body/div/div/div/div/div[3]/div/div/table/tbody/tr['+str(i)+']/td[2]')[0].text[:-1])
            return ((b-a)/a)

def stock(code):
    print(stock1(code),stock2(code))



with open('D://CWSJ.csv', 'w', newline='',encoding='utf-8-sig') as csv_file:
    for i in name:
        csv_writer = csv.writer(csv_file)
        # csv_writer.writerow(('标题', '摘要', '类型', '内容'))
        # print(content)
        three=stock1(name[i])
        csv_writer.writerow((i,three[0],three[1],three[2],stock2(name[i])))



# print('东方环宇')
# stock('603706.SH')






