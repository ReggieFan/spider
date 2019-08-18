# -*- coding: utf-8 -*-
import os
# Scrapy settings for fintech project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'fintech'

SPIDER_MODULES = ['fintech.spiders']
NEWSPIDER_MODULE = 'fintech.spiders'

# HTTPERROR_ALLOWED_CODES = [403]#上面报的是403，就把403加入。

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fintech (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# 解决中文乱码问题
FEED_EXPORT_ENCODING = 'UTF-8'
# FEED_EXPORT_ENCODING = 'gb18030'
ITEM_PIPELINES = {
    'fintech.pipelines.MongoPipeline': 300
}

DOWNLOADER_MIDDLEWARES = {
    'fintech.middlewares.ProxyMiddleware': 555
}

# mongodb数据库配置信息
MONGO_URI = 'localhost'
MONGO_DB = 'big_data'
# 代理获取地址
PROXY_URL = 'http://localhost:5555/random'

# 设置IP池和用户代理

#  允许本地Cookie
COOKIES_ENABLED = False

# 这部分是爬取图片时需要的设置
# 打开image pipeline
# ITEM_PIPELINES = {'fintech.baiduimagespipelines.BaiduimagesPipeline': 1}
# DOWNLOADER_MIDDLEWARES = {'fintech.baidumiddlewares.BaiduImages': 1,}
# # 30 days of delay for images expiration
# IMAGES_EXPIRES = 30
# #设置存放图片的路径
# IMAGES_STORE = 'D:\images\\'
#图片大小
# IMAGES_MIN_HEIGHT = 100
# IMAGES_MIN_WIDTH = 100
# 这部分是爬取图片时需要的设置



# 设置IP池
# IPPOOL = [
#     {"ipaddr": "221.230.72.165:80"},
#     {"ipaddr": "175.154.50.162:8118"},
#     {"ipaddr": "111.155.116.212:8123"}
# ]
#
# # 设置用户代理池
# UPPOOL = [
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
# ]
