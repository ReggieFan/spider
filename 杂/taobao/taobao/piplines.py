class taobaoPipeline(object):
    def process_item(self, item, spider):
        title = item['title'][0]
        link = item['link']
        price = item['price'][0]
        comment = item['comment'][0]
        print('商品名字', title)
        print('商品链接', link)
        print('商品正常价格', price)
        print('商品评论数量', comment)
        print('------------------------------\n')
        return item