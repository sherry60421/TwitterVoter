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

        #發推時間
        self.timeUp = ''

    def isInt(self, value):
        try:
            int(value)
            return True
        except:
            return False
        
    def initLogging(self):
        logging.basicConfig(
                        level    = logging.ERROR,
                        format   = '%(levelname)-8s %(message)s',
                        datefmt  = '%m-%d %H:%M',
                        filename = './Voter.log',
                        filemode = 'w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.ERROR)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        self.logger = logging.getLogger('')

    def initDescription(self):
        print "Let's Joy~"
        print "這支程式為避免被發現是機器人(我也不知道怎麼樣可以發現)"
        print "所以發推的頻率不固定, 大概會在1~10秒之間"
        print "請勿外流啊啊啊"
        print "另外, 姐會寫code就是任性<(￣︶￣)>"
        print "已經寫死發推內容了, 只准你給我投黨首大人啊!!!"
        print "請確認看過使用教學再用,我沒有多餘時間做太多例外處理QQ"
        print "教學: https://sherry60421.gitbooks.io/voter/content/ "
        print ""
        print "--------------------------------------------"
        print ""

    def defineTimeUp(self):
        while True:
            print("若要結束程式請輸入bye")
            self.timeUp = raw_input("請輸入您要自動發推的時間(1~60 mins):")
            if self.timeUp == 'bye':
                exit()
            elif self.isInt(self.timeUp) is False:
                print ('這不是數字!')
            elif int(self.timeUp) > 60:
                print ('不要給大於60的數字啊')
            elif int(self.timeUp) < 1:
                print ('不要給小於1的數字啊')
            else:
                self.timeUp = int(self.timeUp)
                break
        
    def readConfig(self):
        try:
            f = open('config.txt', 'r')
            for line in f.read().split('\n'):
                if 'CONSUMER_KEY=' in line:
                    self.consumer_key = line.split('CONSUMER_KEY=')[1]
                if 'CONSUMER_SECRET=' in line:
                    self.consumer_secret = line.split('CONSUMER_SECRET=')[1]
                if 'ACCESS_TOKEN=' in line:
                    self.access_token = line.split('ACCESS_TOKEN=')[1]
                if 'ACCESS_TOKEN_SECRET=' in line:
                    self.access_token_secret = line.split('ACCESS_TOKEN_SECRET=')[1]
            if self.consumer_key == '' or self.consumer_secret == '' or self.access_token == '' or self.access_token_secret == '':
                self.logger.error('Error occured while readConfig ... return false!')
                return False
            else:
                return True
        except Exception as inst:
            print ('發生一些錯誤, 請提供log檔')
            self.logger.error('Error occured while readConfig ...')
            self.logger.error(type(inst))
            self.logger.error(inst.args)
            self.logger.error('------')
            
    def getRandomEmotion(self):
        return self.emotions[int(random.uniform(0, self.emotionsCount))]
    
    def processHey(self):
        start_time = time.time()
        print ('現在時間 %s ' % time.ctime(start_time))
        end_time = start_time + 60 * self.timeUp
        print ('結束時間 %s ' % time.ctime(end_time))
        now = start_time

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        count = 0
        
        while now < end_time:
            try:
                suffix = self.getRandomEmotion()
                text = STATUS + suffix
                api.update_status(status=text)
                pass_time = random.uniform(1, 10)
                now = now + pass_time
                print ('已於 %s 發twitter' % time.ctime(now))
                count = count + 1
                time.sleep(pass_time)
            except Exception as inst:
                print ('發生一些錯誤, 請提供log檔')
                self.logger.error('Error occured while processHey ...')
                self.logger.error(type(inst))
                self.logger.error(inst.args)
                self.logger.error('------')
                break
        
        print ("End! 這段期間您貢獻了 %d 張票!" % count)
        
def process():
    nikukyu = ILoveNikukyu()
    readConfig = nikukyu.readConfig()
    if readConfig == True:
        nikukyu.initDescription()
        while True:
            nikukyu.defineTimeUp()
            nikukyu.processHey()
    else:
        print "讀配置檔發生問題!"
    
if __name__ == '__main__':
    process()
