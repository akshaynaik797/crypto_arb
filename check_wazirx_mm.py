import requests, time
profit = 1.01
var = 10 
url1 = "https://api.wazirx.com/api/v2/tickers"
mylist = ['BTC', 'XRP', 'USDT', 'ETH', 'TRX', 'LTC', 'WRX']
while(1):
    try:
        data = requests.get(url1)
        data = data.json()
        timestamp = time.time()
        for i in mylist:
            i = i.lower()+'inr'
            if float(data[i]['sell']) > float(data[i]['buy'])*profit:
#                print(data[i]['sell'], data[i]['buy'])
                print(i)
        print()
        time.sleep(1)
    except Exception as error:
        print(error,f", error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
