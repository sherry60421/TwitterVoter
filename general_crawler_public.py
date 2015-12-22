# -*- coding: utf-8 -*-
##################################################################################
#                                                                                #
#  Copyright (c) 2014 Yao Nien, Yang, paulyang0125@gmail.com                     #  
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not   #
#  use this file except in compliance with the License. You may obtain a copy    #
#  of the License at http://www.apache.org/licenses/LICENSE-2.0. Unless required #
#  by applicable law or agreed to in writing, software distributed under the     #
#  License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS  #
#  OF ANY KIND, either express or implied. See the License for the specific      #
#  language governing permissions and limitations under the License.             # 
#                                                                                #
##################################################################################

import bs4
import urllib.request
import re
import time
import logging
import json
from optparse import OptionParser
from optparse import Option, OptionValueError
import os, sys

LOGPATH = 'C:/Users/188045/Desktop/crawler_codelog'
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
        ## debug flag to enable debug - not finished yet.
        self.path = LOGPATH
        self.rootPage = lambda id:''+id
        
        self.initLogging()

        self.num_pushes = dict()
        os.chdir(self.path)
        
    def initLogging(self):
        '''
        initializing logging function and put to /Crawler.log
        '''
        myLogPath = self.path

        print ("initializing the logging .......")
        try:
            os.makedirs(myLogPath)
        except: 
            sys.stderr.write('Warning: "%s" already existed\n' % myLogPath)
        LOGPATH = myLogPath + '/' + LOGNAME + '.log'
        #logger.warn('Warning: "%s" already existed\n' % myLogPath)
        self.logger = logging.getLogger('web crawler')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr = logging.FileHandler(LOGPATH)
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr) 
        #logger.setLevel(logging.DEBUG)
        self.logger.info('web crawler started')
    
    def remove_html_tags(self, data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)
    
    def closeLogging(self):
        self.logger.info('closing logging')
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)
    
    def getContent(self):

        ## link to mySQL
        '''
        db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
        cursor = db.cursor()
        '''
        start_time = time.time()
  
        for indexP in range(startIndex, endIndex):
            sys.stderr.write('start from index %s ...\n' % indexP)
            self.logger.debug('start from index %s ...\n' % indexP)
            try:
                page = bs4.BeautifulSoup(urllib.request.urlopen(self.rootPage(indexP)).read())

                # run sql query
                '''
                sql = ("INSERT INTO " + TABLE_NAME + " (title,author,postTime,link,content,haveName,haveEatTime,havePhone,"
                    "haveAddress,haveOpenTime,havePrice,haveBoxInfo,haveCreditCard,haveRecommendPlate,"
                    "haveWebsite,name,eatTime,phone,address,openTime,price,boxInfo,creditCard,"
                    "recommendPlate,website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,"
                    " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                arguments = [title, author, postTime, link, content, haveName, haveEatTime, havePhone, haveAddress,
                haveOpenTime, havePrice, haveBoxInfo, haveCreditCard, haveRecommendPlate, haveWebsite,
                name, eatTime, phone, address, openTime, price, boxInfo, creditCard, recommendPlate, website]

                cursor.execute(sql, arguments)
                db.commit()
                '''
                time.sleep(0.1)
            except:
                sys.stderr.write('Error occured while fetching %s\n' % self.rootPage(indexP))
                self.logger.error('Error occured while fetching %s\n' % self.rootPage(indexP))
            
        '''            
        cursor.close()
        db.close()
        '''
        ## do the final logging and printing all numbers     
        self.logger.info('Ending crawling ... !! \n')
        self.logger.info('\n')
        self.closeLogging()
        elapsed_time = time.time() - start_time
        print ("elapsed time: %s" % elapsed_time)

def process():
    #print options.commands[0]
    #print args[0]

    print ("getting all index...")
    crawler = Crawler()
    crawler.getContent()

if __name__ == '__main__':
    process()

        
