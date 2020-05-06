import time
from datetime import datetime
from arb_assets import fetch_bitbns_prices, check_for_triarb
pairlist = [
            ['INR', 'USDT', 'BTC', 'INR'],
            ['INR', 'BTC', 'USDT', 'INR'],
            ['INR', 'USDT', 'ETH', 'INR'],
            ['INR', 'ETH', 'USDT', 'INR'],
]

while(1):
    try:
        prices = fetch_bitbns_prices()
#        for pairs in pairlist:
#            record = check_for_triarb(pairs, prices)
#            if record[0]/record[1]*100-100 > 0.9:
#                print(record)
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("bitbns.csv", "a") as fp:
            fp.write(f"{timestamp}, {prices}"+'\n')
        time.sleep(1)
        var = 10
    except:
        print(f"error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
