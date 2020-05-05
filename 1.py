import time
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
        for pairs in pairlist:
            print(check_for_triarb(pairs, prices))
        print()
        time.sleep(1)
        var = 10
    except:
        time.sleep(var)
        var = var*1.1
