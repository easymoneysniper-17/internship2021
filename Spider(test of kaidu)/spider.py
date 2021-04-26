import requests
import csv
import pandas as pd
import datetime
import time


#下载pdf公告的函数
def downloadpdf(url, file):
    resp = requests.get(url)
    f = open(file, 'wb')
    f.write(resp.content)
    f.close()

data = pd.read_csv("年报/爬取报告_20200106-20210105.csv")

for i in range(0,6731):
    try:
        filename = str(datetime.datetime.strptime(data.loc[i][3],'%Y/%m/%d %H:%M').date()) + '+' +'{:0>6}'.format(str(data.loc[i][0])) + str(data.loc[i][1]) + '+' + str(data.loc[i][2])
        url = data.loc[i][4]
        downloadpdf(url=url, file=filename)
    except:
        url = data.loc[i][4]
        print('出问题的网址'+url)

