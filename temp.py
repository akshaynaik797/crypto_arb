import json
import re

p = re.compile('(?<!\\\\)\'')

limit = 1.015
pairs = [
         # ['inr', 'usdt', 'btc', 'inr'],
         # ['inr', 'usdt', 'eth', 'inr'],
         # ['inr', 'usdt', 'ltc', 'inr'],
         # ['inr', 'usdt', 'xrp', 'inr'],
         # ['inr', 'usdt', 'trx', 'inr'],
         ['inr', 'usdt', 'btt', 'inr'],
         ['inr', 'usdt', 'bat', 'inr'],
         ['inr', 'usdt', 'ftt', 'inr'],
         # ['inr', 'btc', 'eth', 'inr'],
         # ['inr', 'btc', 'ltc', 'inr'],
         # ['inr', 'btc', 'xrp', 'inr'],
         # ['inr', 'btc', 'trx', 'inr'],
]

def check_for_triarb(pair, data, limit):
    """
        function to validate tri_arb
        pair = a pair like ['inr', 'usdt', 'btc', 'inr']
        data = tick data from url https://api.wazirx.com/api/v2/tickers
        limit = 1.006 or more
    """
    bid = float(data[pair[2]+pair[0]]['buy'])
    ask1 = float(data[pair[2]+pair[1]]['sell'])
    ask2 = float(data[pair[1]+pair[0]]['sell'])
    if bid > ask1*ask2*limit:
        return True
    else:
        pair = pair[::-1]
        bid = float(data[pair[2]+pair[0]]['buy'])
        ask1 = 1/float(data[pair[1]+pair[2]]['buy'])
        ask2 = float(data[pair[1]+pair[0]]['sell'])
        if bid > ask1*ask2*limit:
            return True

with open("wazirx.csv") as fp:
    for i in fp:
        tmp = json.loads(p.sub('\"', i.split('|')[1]))
        for pair in pairs:
            if check_for_triarb(pair, tmp, limit):
                print(pair, i.split('|')[0])