# -*- coding: utf-8 -*-
import bs4
import urllib.request
import re
import time
import json
from optparse import OptionParser
from optparse import Option, OptionValueError
import os, sys
import requests
import csv
from csvvalidator import *

LOGPATH = 'C:/Users/188045/Desktop/crawler_code/log'
LOGNAME = 'WEBlog'
VERSION = '0.2'

## MySQL
HOST = "localhost"
USER = "sa"
PASSWD = "12345"
DB ="test"
CHARSET = 'utf8'

TABLE_NAME = "HoildayCheck"

class Crawler(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.pricePage = 'http://www.custeel.com/sjzx/data/steel_image.jsp'
        self.header = {
            "Host": "jiancai.mysteel.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "X-FirePHP-Version": "0.0.6",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,ja;q=0.2"
            }
        self.loginData = {
            "site":"mysteel",
            "callback":"http://www.mysteel.com/",
            "my_username":"csccom",
            "my_password":"230600",
            "cookietime":"-1",
            "imageField.x":"60",
            "imageField.y":"10"
            }
        self.indexPage = lambda id: 'http://list1.mysteel.com/price/p-10064--01010101--' + str(id) + '.html'
        self.records = []
        self.field = ['date', 'city', 'product', 'category', 'price']
        self.errorPage = []
    
    def remove_html_tags(self, data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)

    def getCookie(self):
        sys.stderr.write('取得cookies...\n')
        s = requests.Session()
        loginUrl = "http://passport.mysteel.com/login.jsp"
        #s.cookies.update(requests.utils.cookiejar_from_dict())
        r = s.post(loginUrl, data=self.loginData, allow_redirects=False)
        self.cookie = r.cookies

    def getUrls(self, rootPage):
        url = []
        resp = requests.get(rootPage, cookies=self.cookie, allow_redirects=False)
        resp.encoding = 'gb2312'
        page = bs4.BeautifulSoup(resp.text, 'html.parser')
        lis = page.find('ul',class_='nlist').find_all('li')
        for li in lis:
            if li.get('class') != None and li['class'] == ['dashed']:
                continue
            url.append(li.find('a')['href'])        
        return url
    
    def getContentPrice(self, url):
        sys.stderr.write('爬價格 %s ...\n' % url)
        resp = requests.get(url, headers=self.header, cookies=self.cookie, timeout=99999)
        resp.encoding = 'gb2312'
        result = bs4.BeautifulSoup(resp.text, 'html.parser')
        main = result.find(id='main')
        #日期
        date = main.find('div', class_='info').get_text()[:10]
        city = []
        category = []
        records = []
        
        table = main.find('table', id='priceTable')
        #取得有幾個不同規格
        categoryNum = len(table.find_all('td',text='涨幅'))
        if categoryNum == 0:
            categoryNum = len(table.find_all('td',text='涨跌'))
            if categoryNum == 0:
                self.errorPage.append(url)
                return
        
        trs = table.find_all('tr')
        #一個規格有幾列資料與之相關
        rows = int((len(trs)-1)/categoryNum)
        #取得城市
        header = trs[0].find_all('td')
        for i in range(0, len(header)):
            if i==0:
                product = header[i].get_text()
            elif i==len(header)-1:
                continue
            else:
                city.append(header[i].get_text())
        #取得規格名
        for i in range(1, len(trs), rows):
            category.append(trs[i].find_all('td')[0].get_text())
        #開始抓
        '''
        結構: field=[date,city,category,price,...]
              record=[[d1,c1,ca1,pr1,...],[],[],...]
        '''
        #先開record出來
        for i in range(1, len(trs), rows):
            tds = trs[i].find_all('td')
            thisCategory = category[int(i/rows)]
            for j in range(1, len(tds)-1):
                record = []
                price = tds[j].get_text()
                thisCity = city[j-1]
                record.append(date)
                record.append(thisCity)
                record.append(product)
                record.append(thisCategory)
                record.append(price)
                records.append(record)
        self.records.extend(records)
    
    def getContent(self):
        
        start_time = time.time()
        self.getCookie()
        sys.stderr.write('開始爬文...\n')
        for p in range(1, 2): #目前共45頁 <-- 應動態處理 TODO
            sys.stderr.write('rootPage : %d ...\n' % p)
            rootPage = self.indexPage(p)
            urls = self.getUrls(rootPage)
            for u in urls:
                self.getContentPrice(u)
                time.sleep(0.3)
            time.sleep(0.5)

        #寫入檔案
        
        #f = open("stock.csv","w")

        #display
        print ("%s\t%s\t%s\t%s\t%s" % (self.field[0], self.field[1], self.field[2], self.field[3], self.field[4]))
        print ("-------------------------------------------------------------------")
        for r in self.records:
            print ("%s\t%s\t%s\t%s\t%s" % (r[0], r[1], r[2], r[3], r[4]))

        print(errorPage)
        elapsed_time = time.time() - start_time
        print ("elapsed time: %s" % elapsed_time)

def process():
    crawler = Crawler()
    crawler.getContent()

if __name__ == '__main__':
    process()

        
