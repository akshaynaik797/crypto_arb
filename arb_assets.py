import requests

def fetch_bitbns_prices():
    url1 = "https://bitbns.com/order/getTickerWithVolume/"
    data = requests.get(url1)
    data = data.json()
    prices = {
              'BTCINR':{'ask':data['BTC']['lowest_sell_bid'],
                        'bid':data['BTC']['highest_buy_bid']},
              'INRBTC':{'bid':1/data['BTC']['lowest_sell_bid'],
                        'ask':1/data['BTC']['highest_buy_bid']},

              'USDTINR':{'ask':data['USDT']['lowest_sell_bid'],
                        'bid':data['USDT']['highest_buy_bid']},
              'INRUSDT':{'bid':1/data['USDT']['lowest_sell_bid'],
                        'ask':1/data['USDT']['highest_buy_bid']},

              'ETHINR':{'ask':data['ETH']['lowest_sell_bid'],
                        'bid':data['ETH']['highest_buy_bid']},
              'INRETH':{'bid':1/data['ETH']['lowest_sell_bid'],
                        'ask':1/data['ETH']['highest_buy_bid']},

              'ETHUSDT':{'ask':data['ETHUSDT']['lowest_sell_bid'],
                        'bid':data['ETHUSDT']['highest_buy_bid']},
              'USDTETH':{'bid':1/data['ETHUSDT']['lowest_sell_bid'],
                        'ask':1/data['ETHUSDT']['highest_buy_bid']},

              'BTCUSDT':{'ask':data['BTCUSDT']['lowest_sell_bid'],
                        'bid':data['BTCUSDT']['highest_buy_bid']},
              'USDTBTC':{'bid':1/data['BTCUSDT']['lowest_sell_bid'],
                        'ask':1/data['BTCUSDT']['highest_buy_bid']}}
    return prices

pairs = ['INR', 'USDT', 'BTC']
def check_for_triarb(pairs, prices):
    a = prices[pairs[2]+pairs[0]]['bid']
    b = prices[pairs[2]+pairs[1]]['ask']*prices[(pairs[1]+pairs[0])]['ask']
    return (a, b, pairs)
