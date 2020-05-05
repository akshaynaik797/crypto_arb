import requests, time, json
url1 = " https://api.binance.com/api/v3/depth"
param1 = {"symbol":"BTCUSDT", "limit":5}
url2 = "https://api.wazirx.com/api/v2/depth?market=btcusdt"
usdt1, usdt2, inr1, inr2 = 9000, 9000, 1, 1


while(1):

    try:
        data = requests.get(url=url1, params=param1).json()
        ask1, bid1 = float(data['asks'][0][0]), float(data['bids'][0][0])
        var = 10
    except:
        time.sleep(var)
        var = var*1.1

    try:
        data = requests.get(url2)
        data = data.json()
        ask2, bid2 = float(data['asks'][0][0]), float(data['bids'][0][0])
        var = 10
    except:
        time.sleep(var)
        var = var*1.1


    if bid1 > ask2:
        if usdt2 != 0:
            usdt2 = usdt2+(inr2/ask2)
            inr2 = 0
        if inr1 != 0:
            inr1 = inr1+(bid1*usdt1)
            usdt1 = 0
            record = f"{ask1}, {bid1}, {ask2}, {bid2}, {usdt1}, {inr1}, {usdt2}, {inr2}"
            print(record)
            with open("log.csv", "a") as fp:
               fp.write(record+'\n')
    elif bid2 > ask1:
        if usdt1 != 0:
            usdt1 = usdt1+(inr1/ask1)
            inr1 = 0
        if inr2 != 0:
            inr2 = inr2+(bid2*usdt2)
            usdt2 = 0
            record = f"{ask1}, {bid1}, {ask2}, {bid2}, {usdt1}, {inr1}, {usdt2}, {inr2}"
            print(record+'\n')
            with open("log.csv", "a") as fp:
               fp.write(record)
    time.sleep(1)

