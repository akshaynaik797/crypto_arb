"""
    script contains function for validate tri_arb existance on wazirx
"""
#pairs to check for tri_arb
pairs = [
         ['inr', 'usdt', 'btc', 'inr'],
         ['inr', 'usdt', 'eth', 'inr'],
         ['inr', 'usdt', 'ltc', 'inr'],
         ['inr', 'usdt', 'xrp', 'inr'],
         ['inr', 'usdt', 'trx', 'inr'],
         ['inr', 'btc', 'eth', 'inr'],
         ['inr', 'btc', 'ltc', 'inr'],
         ['inr', 'btc', 'xrp', 'inr'],
         ['inr', 'btc', 'trx', 'inr'],
]

def check_for_triarb(pair, data, limit):
    """
        function to validate tri_arb
        pair = a pair like ['inr', 'usdt', 'btc', 'inr']
        data = tick data from url https://api.wazirx.com/api/v2/tickers
        limit = 1.006 or more 
    """
    limit = limit
    bid = float(data[pair[2]+pair[0]]['buy'])
    ask1 = float(data[pair[2]+pair[1]]['sell'])
    ask2 = float(data[pair[1]+pair[0]]['sell'])
    if bid > ask1*ask2*limit:
        return 1
    else:
        pair = pair[::-1]
        bid = float(data[pair[2]+pair[0]]['buy'])
        ask1 = 1/float(data[pair[1]+pair[2]]['buy'])
        ask2 = float(data[pair[1]+pair[0]]['sell'])
        if bid > ask1*ask2*limit:
            return 1

