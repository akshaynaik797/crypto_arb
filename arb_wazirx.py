import pymongo, json
from datetime import datetime
from pprint import pprint
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol = mydb["wazirx"]
docs = mycol.find()
for a in docs:
    bid = float(a['prices']['ltcinr']['sell'])
    ask1 = float(a['prices']['ltcusdt']['buy'])
    ask2 = float(a['prices']['usdtinr']['buy'])
    timestamp = datetime.fromtimestamp(float(a['_id'])).isoformat()
    asks = ask1*ask2
    if bid > asks*1.008:
        ratio = round(bid/asks*100-100, 2)
        print(f"{timestamp[11:19]}, {round(bid, 2)}, {round(asks, 2)}, {ratio}")
