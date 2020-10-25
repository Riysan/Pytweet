# coding: UTF-8
 
import json
from requests_oauthlib import OAuth1Session
 
#API_KEY / Tweet --------------------------------------------
tweet = "Twitter for Python" #Tweet
CK = "***"
CS = "***"
AT = "***"
AS = "***"
#------------------------------------------------------------

tw = OAuth1Session(CK, CS, AT, AS)
url = "https://api.twitter.com/1.1/statuses/update.json"
params  {"status" : tweet}
req = tw.post(url, params = params) 
if req.status_code == 200:
    print("200 OK")
else: 
    print("ERROR : " req.status_code) 
