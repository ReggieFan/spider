from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re

class BaiduimagesPipeline(ImagesPipeline):
# 不知道为什么不能加keyword
    def get_media_requests(self, item, info):
        yield Request(item["image_urls"], meta={'name': item['image_name'],
                                                'keyword':item['keyword']})

    # 重命名的功能 重写此功能可以得到自己想要文件名称 否则就是uuid的随机字符串
    def file_path(self, request, response=None, info=None):
        # 图片名称
        # img_name = request.url.split('/')[-1]
        # 图片分类的名称
        name = request.meta['name']
        keyword=request.meta['keyword']
        # 处理特殊字符串
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        # 重命名图片名字
        # print (keyword)
        filename = u'{0}/{1}.jpg'.format(keyword,name)
        # print (filename)
        return filename

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     # 上面的表达式等于
    #     # for ok,x in results:
    #     #     if ok:
    #     #         print(x['path'])
    #     if not image_paths:
    #         raise DropItem('Item contains no images')
    #     item['image_urls'] = image_paths
    #     return item