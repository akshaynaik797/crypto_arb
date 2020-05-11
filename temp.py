import requests, time
import pymongo, json
from datetime import datetime
from pprint import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol = mydb["bitbns"]
docs = mycol.find()
var = 10

pairs = [
         ['INR', 'USDT', 'BTC', 'INR'],
         ['INR', 'USDT', 'ETH', 'INR'],
         ['INR', 'USDT', 'LTC', 'INR'],
         ['INR', 'USDT', 'XRP', 'INR'],
         ['INR', 'USDT', 'TRX', 'INR'],
]

def check_for_triarb(pair, data):
    limit = 1.006
    bid = data[pair[2]]['highest_buy_bid']
    ask1 = data[pair[2]+pair[1]]['lowest_sell_bid']
    ask2 = data[pair[1]]['lowest_sell_bid']
    if bid > ask1*ask2*limit:
        print(pair)
    else:
        pair = pair[::-1]
        bid = data[pair[2]]['highest_buy_bid']
        ask1 = 1/data[pair[1]+pair[2]]['highest_buy_bid']
        ask2 = data[pair[1]]['lowest_sell_bid']
        if bid > ask1*ask2*limit:
            print(pair)

for i in docs:
    data = i['prices']
    timestamp = datetime.fromtimestamp(float(i['_id'])).isoformat()
    for j in pairs:
        if check_for_triarb(j, data):
            print(timestamp)
            check_for_triarb(j, data)
            
