#-*-coding:utf-8-*-
import csv
import json
import sys
import codecs
import jsonlines
import os


for i in os.walk(r'D:\fintech\\'):
    # print(i)
    count = 1
    for j in i[2]:
        print(str(count/len(i[2]) * 100) + '%')
        count+=1
        print(j)
        csvfile = open(r'D:\fintech2\\'+j[:-4]+'.csv', 'w', newline='',encoding='utf-8-sig')  # python3下
        writer = csv.writer(csvfile)
        jsonData = open(r'D:\fintech\\'+j, "r+", encoding="utf-8-sig")
# csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
# csvfile = open(path+'.csv', 'wb') # python2下
        try:
            flag = True
            for line in jsonlines.Reader(jsonData):
                dic = line
                if flag:
                    # 获取属性列表
                    keys = list(dic.keys())
                    print (keys)
                    writer.writerow(keys) # 将属性列表写入csv中
                    flag = False
                val=list(dic.values())
                print (val)
                writer.writerow(tuple(val))
        except:
            print(j+'Error!!')
        jsonData.close()
        csvfile.close()
