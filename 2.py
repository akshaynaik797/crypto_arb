import time, json
from datetime import datetime
from arb_assets import fetch_bitbns_prices, check_for_triarb
pairlist = [
            ['INR', 'USDT', 'BTC', 'INR'],
            ['INR', 'BTC', 'USDT', 'INR'],
            ['INR', 'USDT', 'ETH', 'INR'],
            ['INR', 'ETH', 'USDT', 'INR'],
]

with open("bitbns.csv") as fp:
    b = fp.readlines()
    for a in b:
        prices = json.loads(a[a.find('{'):].strip('\n').replace('\'','\"'))
        for pairs in pairlist:
            record = check_for_triarb(pairs, prices)
            if record[0]/record[1]*100-100 > 0.9:
                print(f"{record}, {record[0]/record[1]*100-100}")
