# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import time
import os, sys
import requests

class Crawler(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.rootPage = 'http://www.japaneseemoticons.org/amazed/'

    def getUrls(self, rootPage):
        url = []
        resp = requests.get(rootPage)
        resp.encoding = 'utf-8'
        page = BeautifulSoup(resp.text, 'html.parser')
        
        lis = page.find('div',class_='execphpwidget').find_all('li')
        for li in lis:
            url.append(li.find('a')['href'].encode('utf8'))        
        return url
    
    def getContentText(self, url):
        #print ('爬內容 %s ...' % url)
        resp = requests.get(url, timeout=99999)
        resp.encoding = 'utf-8'
        result = BeautifulSoup(resp.text, 'html.parser')
        main = result.find('div', class_='entry-content').find('p').get_text().encode('utf8')
        return main
    
    def getContent(self):
        
        start_time = time.time()
        f = open('emotions.txt', 'w')
        print ('開始爬文...')
        print ('rootPage : %s ...' % self.rootPage)
        urls = self.getUrls(self.rootPage)
        for u in urls:
            print (u)
            mainEmotions = self.getContentText(u)
            f.write(mainEmotions + '\n')
            time.sleep(0.3)
        f.closed

        elapsed_time = time.time() - start_time
        print ("elapsed time: %s" % elapsed_time)

def process():
    crawler = Crawler()
    crawler.getContent()

if __name__ == '__main__':
    process()

        
