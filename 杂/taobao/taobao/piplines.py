class taobaoPipeline(object):
    def process_item(self, item, spider):
        title = item['title'][0]
        link = item['link']
        price = item['price'][0]
        comment = item['comment'][0]
        print('��Ʒ����', title)
        print('��Ʒ����', link)
        print('��Ʒ�����۸�', price)
        print('��Ʒ��������', comment)
        print('------------------------------\n')
        return item