import requests
import re
import urllib.robotparser

url = 'https://s.taobao.com/search?q=书包&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44'
headers={
'authority':'s.taobao.com',
'method':'GET',
'path':'/search?q=%E4%B9%A6%E5%8C%85&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44',
'scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'accept-encoding':'gzip, deflate, sdch',
'accept-language':'zh-CN,zh;q=0.8',
'cache-control':'max-age=0',
'cookie':'cna=gscLFYiiZWUCAd7Js1AjzTZF; enc=iriYfMOh3BqlqrcxgH7tpl0E7qKm15uK87w4uZBnX%2Fa1cY%2BI36gVrp4iohp8mzQ2vaTBJoAwlpryx8FJ1cytsw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=586556481886464373; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; _tb_token_=Jlg7Uvzp9kWES5MPyoMX; v=0; unb=2998033707; uc3=nk2=DN9io9s1hTRzh86xkg%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&vt3=F8dBy32ghvdZ6XQMd1o%3D&id2=UUGrfolO4Dxs7g%3D%3D; csg=a68b47c4; lgc=onion66591813; t=79bfde8a26854e0de729d3edf4ba39a7; cookie17=UUGrfolO4Dxs7g%3D%3D; dnk=onion66591813; skt=04a3af04a7806b92; cookie2=189a88152be2c9fb25d63bc4a8ea8df3; existShop=MTU2NTA1ODA3MQ%3D%3D; uc4=id4=0%40U2OcTk%2BbAq5VXB7CuMB5IOSYTdbS&nk4=0%40DsiGbdHMyUymq%2Fc7U83mpiiFVgcve4FN; tracknick=onion66591813; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=37f; _nk_=onion66591813; cookie1=BxUALWDUFgCM%2Fs%2BEatdt5JjvPN%2FPtV3A%2F2QUmpiRQ8E%3D; mt=ci=35_1; _m_h5_tk=21a1640af998b0375a833fba6ee915fa_1565065273400; _m_h5_tk_enc=5d2f963f9da834de81f1c99828a531e6; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTaHY70DBnuyQ%3D%3D&lng=zh_CN&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&existShop=false&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&tag=8&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0; JSESSIONID=05FD7989EDACDA93078A0F49A29344A5; isg=BJ2dqq8SnHSmIXmZCbHacZFtonmXutEMmMCt5V9i2PQjFr1IJwmz3HyNREq11unE; l=cBSGQrXevXsQx4NOBOCZhurza779sBdAguPzaNbMi_5dU6Yskm7Ok5ISuFv6cjWdtsYB42kASYJ9-etkTp206Pt-g3fP.',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
       }
rp = urllib.robotparser.RobotFileParser()
print(rp.can_fetch(headers, url))
r = requests.get(url, timeout = 30, headers=headers)
# print(r.text)
r.raise_for_status()
r.encoding = r.apparent_encoding
# print(r.text)
html=r.text

plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
print(plt,tlt)