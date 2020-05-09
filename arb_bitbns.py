import pymongo, json
from datetime import datetime
from pprint import pprint
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol = mydb["bitbns"]
docs = mycol.find()
#lowest_sell_bid = ask
#highest_buy_bid = bid
for a in docs:
    bid = float(a['prices']['BTC']['highest_buy_bid'])
    ask1 = float(a['prices']['BTCUSDT']['lowest_sell_bid'])
    ask2 = float(a['prices']['USDT']['lowest_sell_bid'])
    timestamp = datetime.fromtimestamp(float(a['_id'])).isoformat()
    asks = ask1*ask2
    if bid > asks*1.006:
        ratio = round(bid/asks*100-100, 2)
        print(f"{timestamp[:19]}, {round(bid, 2)}, {round(asks, 2)}, {ratio}")
