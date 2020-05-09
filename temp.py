import pymongo, json
from datetime import datetime
from pprint import pprint
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol0, mycol1 = mydb["bitbns"], mydb["wazirx"]
bitbns, wazirx = mycol0.find(), mycol1.find()
#lowest_sell_bid = ask
#highest_buy_bid = bid
#sell = bid
#buy = ask
a, b = 'trxinr', 'TRX'
for i, j in zip(bitbns, wazirx):
        time1 = float(i['_id'])
        time1 = datetime.fromtimestamp(float(i['_id'])).isoformat()
        time2 = float(j['_id'])
        time2 = datetime.fromtimestamp(float(j['_id'])).isoformat()
        print(time1, time2)
