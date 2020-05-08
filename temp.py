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
a, b = 'ltcinr', 'LTC'
for i in range(wazirx.count()):
    bid1 = float(wazirx[i]['prices'][a]['sell'])
    ask1 = float(bitbns[i]['prices'][b]['lowest_sell_bid'])

    ask2 = float(wazirx[i]['prices'][a]['buy'])
    bid2 = float(bitbns[i]['prices'][b]['highest_buy_bid'])
    timestamp = datetime.fromtimestamp(float(wazirx[i]['_id'])).isoformat()
    if bid1 > ask1*1.006:
        ratio = round(bid1/ask1*100-100, 2)
        print(f"{timestamp[11:19]}, {round(bid1, 2)}, {round(ask1, 2)}, {ratio} buy bit sell wazir")
    elif bid2 > ask2*1.006:
        ratio = round(bid2/ask2*100-100, 2)
        print(f"{timestamp[11:19]}, {round(bid2, 2)}, {round(ask2, 2)}, {ratio} buy wazir sell bit")

