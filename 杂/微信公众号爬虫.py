import wechatsogou

# 可配置参数
# 直连
wechats = wechatsogou.WechatSogouAPI()
# wechats = wechatsogou.WechatSogouApi()
name = '华工校园'
# wechat_infos = wechats.search_gzh_info(name)
# info=wechats.get_gzh_info(name)
article=wechats.search_article('南京航空航天大学')
# print(article)
for i in article:
    print(i)
# print(info)

