url1 = "https://bitbns.com/order/getTickerWithVolume/"
"""
    script contains function for validate tri_arb existance on bitbns
"""
#pairs to check for tri_arb
pairs = [
         ['INR', 'USDT', 'BTC', 'INR'],
         ['INR', 'USDT', 'ETH', 'INR'],
         ['INR', 'USDT', 'LTC', 'INR'],
         ['INR', 'USDT', 'XRP', 'INR'],
         ['INR', 'USDT', 'TRX', 'INR'],
]

def check_for_triarb(pair, data):
    """
        function to validate tri_arb
        pair = a pair like ['INR', 'USDT', 'BTC', 'INR']
        data = tick data from url https://bitbns.com/order/getTickerWithVolume/
    """
    limit = 1.008
    bid = data[pair[2]]['highest_buy_bid']
    ask1 = data[pair[2]+pair[1]]['lowest_sell_bid']
    ask2 = data[pair[1]]['lowest_sell_bid']
    if bid > ask1*ask2*limit:
        return 1
    else:
        pair = pair[::-1]
        bid = data[pair[2]]['highest_buy_bid']
        ask1 = 1/data[pair[1]+pair[2]]['highest_buy_bid']
        ask2 = data[pair[1]]['lowest_sell_bid']
        if bid > ask1*ask2*limit:
            return 1

