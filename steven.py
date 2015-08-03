import requests
import argparse
import json
import urllib2
import ssl
import sys
# enterpriseKey = 'ENTa893aebf1fa548c434d083eb359457aa'
# customerKey = 'CUSTa893aebf1fa548c434d083eb359457aa'
# id1 = '54b604dfa520e02948a0f4f1'
# id2 = '54b604dfa520e02948a0f4f9'
# id3 = '54b604dfa520e02948a0f4fd'
# url = 'http://api.reimaginebanking.com/'
# requestString = url + 'customers/' + id1 + '/accounts/'  + customerKey
# body = {"type": "checking", "nickname": "yo", "rewards":1, "balance": 0}
# body = json.dumps(body)
# req = requests.post(requestString, data=body)
# req = requests.get(requestString)
# print(req.text)

# req.json()

apiEndpoint = "https://http-api.openbloomberg.com/"
thingie = "/request/blp/refdata/HistoricalData"
body = { "securities": ["IBM US Equity", "AAPL US Equity"],
  "fields": ["PX_LAST", "OPEN"],
  "startDate": "20120101",
  "endDate": "20120105",
  "periodicitySelection": "DAILY" } 
parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.parse_args()

req = urllib2.Request('https://{}/reguest/blp/refdata/HistoricalData'.format(parser.parse_args()))
req.add_header('Content-Type', 'application/json')
ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.load_verify_locations('bloomberg.crt')
ctx.load_cert_chain('vthacks_spring_2015_018.crt', 'vthacks_spring_2015_018.key')

res = urllib2.urlopen(req, data=json.dumps(body), context=ctx)





