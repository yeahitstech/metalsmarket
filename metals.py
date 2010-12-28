#!/usr/bin/python

import tweepy
import httplib
import string
import time

results = []

def PullNYMetalPrices():
    global results
    results = []
    metals = ['GOLD','SILVER','PLATINUM','PALLADIUM']

    conn = httplib.HTTPConnection("www.kitco.com")
    conn.request("GET", "/market/")
    r1 = conn.getresponse()
    data1 = r1.read()
    conn.close()

    for metal in metals:
        shit = data1.find(metal + '</a></td>')
        key = '<td><p>'
        for x in range(3):
            shit = data1.find('<td>',shit)
	    shit += len(key)
        output = data1[shit:shit+10]
        stopper = output.index('<')
        results.append(metal + ':' + output[:stopper].strip())
    results.append('For more visit: http://www.kitco.com/market/')

def PullWorldMetalPrices():
    global results
    results = []
    metals = ['GOLD','SILVER','PLATINUM','PALLADIUM']

    conn = httplib.HTTPConnection("www.kitco.com")
    conn.request("GET", "/market/")
    r1 = conn.getresponse()
    data1 = r1.read()
    conn.close()

    for metal in metals:
        key = 'The World Spot Price'
        shit = data1.find(key)
	shit += len(key)

        shit = data1.find(metal + '</a></td>')
        shit += len(metal + '</a></td>')
        shit = data1.find(metal + '</a></td>', shit)
     
        key = 'align="center">'
        for x in range(3):
            shit = data1.find(key,shit)
            shit += len(key)
        output = data1[shit:shit+10]
        stopper = output.index('<')
        results.append(metal + ':' + output[:stopper].strip())
    results.append('For more visit: http://www.kitco.com/market/')

def MakePost():
    CONSUMER_KEY = 'czQmrlJVkjKORwGK7pA1Qg'
    CONSUMER_SECRET = 'NeHysTOXfjyRHfnkjOl0RjziF6tRDZOJdQ2linsXWBI'
    ACCESS_KEY = '231007626-523hFRaKWFBtU7vKtSbA5JY9Z6u4bFqwvsgEtWOr'
    ACCESS_SECRET = 'nUneSAAcF48b9rCmPUFAIrsDNfjdpTxIRsdIe3Tcg'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(results)

if time.strftime('%H') in range(9,16):
    PullNyMetalPrices()
else:
    PullWorldMetalPrices()
results.append(time.strftime('%X') + ' EST')
print results
MakePost()
