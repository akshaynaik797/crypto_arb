import requests, time
var = 10
url1 = "https://api.wazirx.com/api/v2/tickers"
pairs = [
         ['inr', 'usdt', 'btc', 'inr'],
         ['inr', 'usdt', 'eth', 'inr'],
         ['inr', 'usdt', 'ltc', 'inr'],
         ['inr', 'usdt', 'xrp', 'inr'],
         ['inr', 'usdt', 'trx', 'inr'],
]

def check_for_triarb(pair, data):
    limit = 1.008
    bid = float(data[pair[2]+pair[0]]['sell'])
    ask1 = float(data[pair[2]+pair[1]]['buy'])
    ask2 = float(data[pair[1]+pair[0]]['buy'])
    if bid > ask1*ask2*limit:
        print(pair)
    else:
        pair = pair[::-1]
        bid = float(data[pair[2]+pair[0]]['sell'])
        ask1 = 1/float(data[pair[1]+pair[2]]['sell'])
        ask2 = float(data[pair[1]+pair[0]]['buy'])
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
