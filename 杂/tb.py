import requests
import re
import urllib.robotparser

def getHTMLText(url):
   try:
       # headers = {
       #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
       # }
       headers = {
           'authority': 's.taobao.com',
           'method': 'GET',
           'path': '/search?q=%E4%B9%A6%E5%8C%85&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, sdch',
           'accept-language': 'zh-CN,zh;q=0.8',
           'cache-control': 'max-age=0',
           'cookie': 'cna=gscLFYiiZWUCAd7Js1AjzTZF; enc=iriYfMOh3BqlqrcxgH7tpl0E7qKm15uK87w4uZBnX%2Fa1cY%2BI36gVrp4iohp8mzQ2vaTBJoAwlpryx8FJ1cytsw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=586556481886464373; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _tb_token_=Jlg7Uvzp9kWES5MPyoMX; v=0; uc3=nk2=DN9io9s1hTRzh86xkg%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dBy32ghvdZ6XQMd1o%3D&id2=UUGrfolO4Dxs7g%3D%3D; csg=a68b47c4; lgc=onion66591813; t=79bfde8a26854e0de729d3edf4ba39a7; dnk=onion66591813; skt=04a3af04a7806b92; cookie2=189a88152be2c9fb25d63bc4a8ea8df3; existShop=MTU2NTA1ODA3MQ%3D%3D; uc4=id4=0%40U2OcTk%2BbAq5VXB7CuMB5IOSYTdbS&nk4=0%40DsiGbdHMyUymq%2Fc7U83mpiiFVgcve4FN; tracknick=onion66591813; _cc_=VT5L2FSpdA%3D%3D; tg=0; mt=ci=35_1; _m_h5_tk=21a1640af998b0375a833fba6ee915fa_1565065273400; _m_h5_tk_enc=5d2f963f9da834de81f1c99828a531e6; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hnT0W0bQmPITBDuZmNpR0tRoIQTY20TDuwu1vrr9kG7JZMb41YGbXy2QQ5uo%2BlqyIqz79%2BC9Ovup08uDstkyn3vnVOET%2Bplv2KDL8TVyzGD9BvDm8UPkTzww4wa4dU8EkeO9wLZDDBPdmkbKUu0%2FeQQOWiQEZj77io%2BthQOc9w%2BXVydpk7tf7iFTh%2BtXtj2Q%2FyoHW8TGJBxFL5HhDOIn56V0pEGPez5oNRPYsrrzVAqUdbRhCwLST%2FwQ%3D%3D; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTaHY748rpFYg%3D%3D&tag=8&lng=zh_CN; _uab_collina=156509190669896365384694; x5sec=7b227365617263686170703b32223a226533383564623333346562613065643361656436333864613639333766643434434f6e5170656f46454d47496a38506639366e5468774561444449354f5467774d7a4d334d4463374d513d3d227d; JSESSIONID=FFB86868D360AEC077987A2EF59870DC; l=cBSGQrXevXsQx_KkBOCalurza779IBdYmuPzaNbMi_5Bz6L6lZQOk5iXaFp6cjWdtOYB42kASYJ9-etkiKy06Pt-g3fP.; isg=BBUVQctf5B1rPcEhwcnSaUk1KhHPEskk0Og1fZe60gzb7jXgX2Fd9ZqsvLJ9auHc',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
       }
       # rp = urllib.robotparser.RobotFileParser()
       # print(rp.can_fetch(headers, url))
       r = requests.get(url, timeout = 30, headers=headers)
       # print(r.text)
       r.raise_for_status()    
       r.encoding = r.apparent_encoding
       return r.text
   except:
       return "获取页面失败"
    
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        # print(plt,tlt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])   #eval可以去掉最外层的引号
            title = eval(tlt[i].split(':')[1])
            if [price,title] not in ilt:
                ilt.append([price,title])
            # print(ilt)
    except:
        print("html中查找信息失败")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = '鞋子'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods + '&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48'
    infoList = []
    # 'https://s.taobao.com/search?q=书包&s=44'
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print('主方法出问题')
    printGoodsList(infoList)

main()
