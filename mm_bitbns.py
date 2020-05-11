import requests, time, os
profit = 1.01
var = 10 
url1 = "https://bitbns.com/order/getTickerWithVolume/"
mylist = ['BTC', 'XRP', 'USDT', 'ETH', 'TRX', 'ZRX', 'LTC']
while(1):
    try:
        data = requests.get(url1)
        data = data.json()
        timestamp = time.time()
        for i in mylist:
            if data[i]['lowest_sell_bid'] > data[i]['highest_buy_bid']*profit:
                print(i)
                os.system('paplay chimes-glassy.ogg &')
        print()
        time.sleep(1)
    except:
        print(f"error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
