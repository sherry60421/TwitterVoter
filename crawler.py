# -*- coding: utf-8 -*-
import tweepy
import time
import sys
import random

STATUS = "http://www.bpnavi.jp/toru/gintama #銀魂PZ_ズンボラ_桂 "
TOKEN = [""
         ,""]

def process():
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
    
    while now < end_time:
        suffix_len = int(random.uniform(1, 10))
        suffix = ''
        for i in range(1, suffix_len + 1):
            suffix = suffix + TOKEN[int(random.uniform(0, 62))]
        text = STATUS + suffix
        api.update_status(status=text)
        pass_time = random.uniform(1, 5)
        now = now + pass_time
        print ""
        time.sleep(pass_time)

    print "End! 要再一次嗎?"
    
if __name__ == '__main__':
    process()
