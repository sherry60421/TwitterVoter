# -*- coding: utf-8 -*-
import tweepy
import time
import sys
import random
import urllib2
import logging

STATUS = "http://www.bpnavi.jp/toru/gintama #銀魂PZ_ズンボラ_桂 "

class ILoveNikukyu(object):
    
    def __init__(self):

        self.initLogging()
        self.prefixText = STATUS
        
        #read emotion file and get every emotion
        emotionsFile = urllib2.urlopen('http://ginduraanthology.web.fc2.com/emotions.txt')
        html = emotionsFile.read()
        self.emotions = []
        for line in html.split('\n'):
            self.emotions.append(line)
        self.emotionsCount = len(self.emotions)

        #config
        self.consumer_key = ''
        self.consumer_secret = ''
        self.access_token = ''
        self.access_token_secret = ''

    def initDesciption(self):
        print "Let's Joy~"
        print "這支程式為避免被發現是機器人(我也不知道怎麼樣可以發現)"
        print "所以發推的頻率不固定, 大概會在1~5秒之間"
        print "請勿外流啊啊啊"
        print "另外, 姐會寫code就是任性<(￣︶￣)>"
        print "已經寫死發推內容了, 只准你給我投黨首大人啊!!!"
        print "請確認看過使用教學再用,我沒有多餘時間做例外處理QQ"
        print "教學:  "
        print ""
        print "--------------------------------------------"
        print ""
        
        while type(self.timeUp) is not int or self.timeUp > 60 or self.timeUp < 1:
            self.timeUp = input("請輸入您要自動發推的時間(1~60 mins):")
            if type(self.timeUp) is not int:
                print ('這不是數字!')
            elif self.timeUp > 60:
                print ('不要給大於60的數字啊')
            elif self.timeUp < 1:
                print ('不要給小於1的數字啊')

    def initLogging(self):
        logging.basicConfig(
                        level    = logging.DEBUG,
                        format   = '%(levelname)-8s %(message)s',
                        datefmt  = '%m-%d %H:%M',
                        filename = './Voter.log',
                        filemode = 'w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        self.logger = logging.getLogger('')
        
    def readConfig(self):
        try:
            f = open('config.txt', 'r')
            for line in f.read().split('\n'):
                if line.contain('CONSUMER_KEY='):
                    self.consumer_key = line.split('CONSUMER_KEY=')[1]
                if line.contain('CONSUMER_SECRET='):
                    self.consumer_secret = line.split('CONSUMER_SECRET=')[1]
                if line.contain('ACCESS_TOKEN='):
                    self.access_token = line.split('ACCESS_TOKEN=')[1]
                if line.contain('ACCESS_TOKEN_SECRET='):
                    self.access_token_secret = line.split('ACCESS_TOKEN_SECRET=')[1]
            if self.consumer_key == '' or self.consumer_secret == '' or self.access_token == '' or self.access_token_secret == '':
                self.logger.error('Error occured while readConfig ... return false! \n')
                return False
            else:
                return True
        except Exception as inst:
            print ('發生一些錯誤, 請提供log檔')
            self.logger.error('Error occured while readConfig ... \n')
            self.logger.error(type(inst))
            self.logger.error(inst.args)
            self.logger.error('------')
            

    def getRandomEmotion(self):
        return self.emotions[int(random.uniform(0, self.emotionsCount))]

    def processHey():
        print "Let's Joy~"
        print "這支程式為避免被發現是機器人(我也不知道怎麼樣可以發現)"
        print "所以發推的頻率不固定, 大概會在1~5秒之間"
        print "請勿外流啊啊啊"
        print "另外, 姐會寫code就是任性<(￣︶￣)>"
        print "已經寫死發推內容了, 只准你給我投黨首大人啊!!!"
        print "請確認看過使用教學再用,我沒有多餘時間做例外處理QQ"
        print "教學:  "
        print ""
        print "--------------------------------------------"
        print ""
        timeUp = input("請輸入您要自動發推的時間(1~60 mins):")

        start_time = time.time()
        end_time = start_time + 60 * timeUp
        now = start_time
        print start_time
        print end_time

        CONSUMER_KEY = 'RMwcjXsQkctidZIpRERy6b28n'
        CONSUMER_SECRET = 'DnWcEAb8KQ5Dzdstc6jf2uUPkXjJ9PWahrvol8QYkdB03ZVK6q'
        ACCESS_TOKEN = '15038191-LqO7J8nWxnsYMvYmEjVjYGHVzvkWa8DS6QjzsEusJ'
        ACCESS_TOKEN_SECRET = 'ux7EnHBkT6n29rEALzBDfjMl92tSRPXFGEPM5rYRhbzNK'

        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        '''
        while now < end_time:
            suffix_len = int(random.uniform(1, 10))
            suffix = ''
            for i in range(1, suffix_len + 1):
                suffix = suffix
            text = STATUS + suffix
            api.update_status(status=text)
            pass_time = random.uniform(1, 5)
            now = now + pass_time
            print ""
            time.sleep(pass_time)
        '''
        print "End! 要再一次嗎?"
        
def process():
    nikukyu = ILoveNikukyu()
    readConfig = nikukyu.readConfig()
    if readConfig == True:
        print (self.consumer_key)
        print (self.consumer_secret)
        print (self.access_token)
        print (self.access_token_secret)
    else:
        print "讀配置檔發生問題!"
    #nikukyu.getRandomEmotion()
    
if __name__ == '__main__':
    process()
