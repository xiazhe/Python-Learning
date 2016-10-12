#-*-coding:utf-8-*-

# 正则
import re
# 网络交互
import requests
# 操作系统功能
import os
import sys
import codecs
from bs4 import BeautifulSoup

# 定义一个类
class Spider:
    #定义一个函数
    def savePageInfo(self, _url, _position, _regX):

        # 要爬的网址
        url = _url
        # 本地地址
        position = _position

        # 获取网页源代码
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser').encode("ascii")

        print(soup)

        html = req.text

        # 正则
        regX = _regX

        pic_url = re.findall(regX,html,re.S)
        print pic_url

        i = 0
        for each in pic_url:
            print each

            pic = requests.get( each )
            print  url + each
            # 如果文件夹不存在，则创建一个文件夹
            if not os.path.isdir(position):

                os.makedirs(position)

            fp = open(position+str(i)+'.jpg', 'wb' )
            fp.write(pic.content)
            # print position+each
            fp.close()
            i+=1


#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝网页爬取图片＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

position_end = ''

# 要爬的网址 http://www.umei.cc/ http://jandan.net/pic
url = 'https://lepture.com/zh/2015/one-week-at-qingdao' + position_end

# 本地地址
position = '/Users/lucker.xia/Desktop/1/' + position_end

# 正则 _'blank\'><img src=(.*?) t'
regX = '<img src=(.*?)'

#参数 url, 储存位置, 爬取的正则
spider = Spider()
spider.savePageInfo(url, position, regX)