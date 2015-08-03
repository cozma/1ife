import requests
import argparse
import json
import urllib2
import ssl
import sys
from pprint import pprint

def getBloomberg(): 
    groceryList = [
            "APD EGGS INDEX",
            "APD WHET INDEX",
            "APD GBEF INDEX",
            "APD BRBL INDEX",
            "APD CABB INDEX",
            "APD BANA INDEX",
            "APD BEAN INDEX",
            "APD CCHS INDEX",
            "APD ROMA INDEX",
            "APD BACO INDEX",
            "APD CHIC INDEX",
            "APD BACO INDEX",
            "APD COFF INDEX",
            "APD RICE INDEX",
            "APD MILK INDEX",
            "APD WHIT INDEX",
            "APD PB INDEX",
            "APD BHAM INDEX",
            "APD BRSK INDEX"
            ]


    apiEndpoint = "https://http-api.openbloomberg.com/"
    thingie = "/request/blp/refdata/HistoricalData"
    body = { "securities": groceryList, 
      "fields": ["PX_LAST", "OPEN"],
      "startDate": "20140101",
      "endDate": "20150105",
      "periodicitySelection": "MONTHLY" } 

    req = urllib2.Request('https://http-api.openbloomberg.com/request/blp/refdata/HistoricalData'.format(apiEndpoint))
    req.add_header('Content-Type', 'application/json')
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('bloomberg.crt')
    ctx.load_cert_chain('vthacks_spring_2015_018.crt', 'vthacks_spring_2015_018.key')

    res = urllib2.urlopen(req, data=json.dumps(body), context=ctx)


    diction = {}
    print "\n"
    for i in range(len(groceryList)):
        body = { "securities": [groceryList[i]], 
          "fields": ["PX_LAST", "OPEN"],
          "startDate": "20140101",
          "endDate": "20150105",
          "periodicitySelection": "MONTHLY" } 
        req = urllib2.Request('https://http-api.openbloomberg.com/request/blp/refdata/HistoricalData'.format(apiEndpoint))
        req.add_header('Content-Type', 'application/json')
        ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        ctx.load_verify_locations('bloomberg.crt')
        ctx.load_cert_chain('vthacks_spring_2015_018.crt', 'vthacks_spring_2015_018.key')
        res = urllib2.urlopen(req, data=json.dumps(body), context=ctx)
        test = json.loads(res.read())

        a = test["data"][0]["securityData"]["security"]
        b = test["data"][0]["securityData"]["fieldData"][0]["PX_LAST"]

        diction[a] = b 
    for i in diction:
        print i, diction[i]
    return diction
getBloomberg()
