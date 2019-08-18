import jsonlines
import os
# path=r'C:\Users\Administrator\Desktop\123'
for i in os.walk(r'C:\Users\Administrator\Desktop\机器学习比赛\爬虫数据\总数据'):
    # print(i)
    count=1
    for j in i[2]:
        print(str(count/len(i[2])*100)+'%')
        print(j)
        count+=1
        try:
            with open(r'C:\Users\Administrator\Desktop\机器学习比赛\爬虫数据\总数据\\'+j, "r+", encoding="utf8") as f:
                with jsonlines.open(r'D:\fintech\\'+j, mode='a') as writer:
                    for item in jsonlines.Reader(f):
                        item['summary']=item.pop('abstract')
                        # print (item)
                        writer.write(item)
                    writer.close()
        except:
            print(j+'出错!!')
