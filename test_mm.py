import pymongo, json
from datetime import datetime
from pprint import pprint
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol0, mycol1 = mydb["bitbns"], mydb["wazirx"]
bitbns, wazirx = mycol0.find(), mycol1.find()
#lowest_sell_bid = ask
#highest_buy_bid = bid
#sell = ask
#buy = bid
a, b = 'trxinr', 'BNB'
templist = []
for i in wazirx:
    timestamp = datetime.fromtimestamp(i['_id']).isoformat()
    ask = float(i['prices'][a]['sell'])
    bid = float(i['prices'][a]['buy'])
    spread = round(ask/bid*100-100, 1)
    templist.append(spread)
    if spread > 1:
        print(spread, timestamp, ask, bid)
print(set(templist))
