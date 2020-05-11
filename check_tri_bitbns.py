import requests, time
var = 10
url1 = "https://bitbns.com/order/getTickerWithVolume/"
pairs = [
         ['INR', 'USDT', 'BTC', 'INR'],
         ['INR', 'USDT', 'ETH', 'INR'],
         ['INR', 'USDT', 'LTC', 'INR'],
         ['INR', 'USDT', 'XRP', 'INR'],
         ['INR', 'USDT', 'TRX', 'INR'],
]

def check_for_triarb(pair, data):
    limit = 1.008
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

while(1):
    data = requests.get(url1)
    try:
        data = data.json()
        for pair in pairs:
            check_for_triarb(pair,data)
        print()
        time.sleep(1)
        var = 10
    except Exception as error:
        print(error,f",error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
