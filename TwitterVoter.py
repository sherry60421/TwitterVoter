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
        sys.stderr.write(u"Let's Joy~\n")
        sys.stderr.write(u"這支程式為避免被發現是機器人(我也不知道怎麼樣可以發現)\n")
        sys.stderr.write(u"所以發推的頻率不固定, 大概會在1~10秒之間\n")
        sys.stderr.write(u"請勿外流啊啊啊\n")
        sys.stderr.write(u"另外, 姐會寫code就是任性<(￣︶￣)>\n")
        sys.stderr.write(u"已經寫死發推內容了, 只准你給我投黨首大人啊!!!\n")
        sys.stderr.write(u"請確認看過使用教學再用,我沒有多餘時間做太多例外處理QQ\n")
        sys.stderr.write(u"教學: https://sherry60421.gitbooks.io/voter/content/ \n")
        sys.stderr.write(u"目前版本: v1.1 \n")
        sys.stderr.write("\n")
        sys.stderr.write("--------------------------------------------\n")
        sys.stderr.write("\n")

    def defineTimeUp(self):
        while True:
            sys.stderr.write(u"請輸入您要自動發推的時間(1~60 mins),若要結束程式請輸入bye:\n")
            self.timeUp = raw_input("")
            if self.timeUp == 'bye':
                exit()
            elif self.isInt(self.timeUp) is False:
                sys.stderr.write(u'這不是數字!\n')
            elif int(self.timeUp) > 60:
                sys.stderr.write(u'不要給大於60的數字啊\n')
            elif int(self.timeUp) < 1:
                sys.stderr.write(u'不要給小於1的數字啊\n')
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
            sys.stderr.write(u'發生一些錯誤, 請提供log檔\n')
            self.logger.error('Error occured while readConfig ...')
            self.logger.error(type(inst))
            self.logger.error(inst.args)
            self.logger.error('------')
            
    def getRandomEmotion(self):
        return self.emotions[int(random.uniform(0, self.emotionsCount))]
    
    def processHey(self):
        start_time = time.time()
        sys.stderr.write(u'現在時間 %s \n' % time.ctime(start_time))
        end_time = start_time + 60 * self.timeUp
        sys.stderr.write(u'結束時間 %s \n' % time.ctime(end_time))
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
                sys.stderr.write(u'已於 %s 發出tweet\n' % time.ctime(now))
                count = count + 1
                time.sleep(pass_time)
            except Exception as inst:
                if str(inst.args[0][0])=="{u'message': u'Status is a duplicate.', u'code': 187}":
                    sys.stderr.write(u'重複tweet內容, 這次先跳過\n')
                    continue
                sys.stderr.write(u'發生一些錯誤, 請提供log檔\n')
                self.logger.error('Error occured while processHey ...')
                self.logger.error(type(inst))
                self.logger.error(inst.args)
                self.logger.error('------')
                break
        
        sys.stderr.write(u"End! 這段期間您貢獻了 %d 張票!\n" % count)
        
def process():
    nikukyu = ILoveNikukyu()
    readConfig = nikukyu.readConfig()
    if readConfig == True:
        nikukyu.initDescription()
        while True:
            nikukyu.defineTimeUp()
            nikukyu.processHey()
    else:
        sys.stderr.write(u"讀配置檔發生問題!\n")
    
if __name__ == '__main__':
    process()
