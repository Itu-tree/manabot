# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

tweet = input('つぶやく内容：')
print('----------------------------------------------------')

params = {"status" : tweet}

req = twitter.post(url, params = params)

if req.status_code == 200:
    print("Succeed")
else:
    print("ERROR : %d"% req.status_code)

