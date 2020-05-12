import requests, pymongo
from datetime import datetime
from tri_wazirx import pairs, check_for_triarb

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["crypto_prices"]
mycol = mydb["wazirx"]
bitbns = mycol.find()

for i in bitbns:
    for pair in pairs:
        if check_for_triarb(pair, i['prices'], 1.006):
            print(datetime.fromtimestamp(i['_id']).isoformat(), pair)
