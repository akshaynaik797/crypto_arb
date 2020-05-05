pairs = ['inr', 'btc', 'usdt']

prices = {
          'usdtinr':{'ask':78.23,
                     'bid':78.00},
          'inrusdt':{'ask':78.23,
                     'bid':78.00},

          'usdtbtc':{'ask':8000,
                     'bid':7990},
          'btcusdt':{'ask':8000,
                     'bid':7990},

          'btcinr':{'ask':710000,
                     'bid':700000},
          'inrbtc':{'ask':710000,
                     'bid':700000},
}

def check_for_triarb(pairs, prices):
    a = prices[pairs[2]+pairs[0]]['bid']
    b = prices[pairs[2]+pairs[1]]['ask']*prices[(pairs[1]+pairs[0])]['ask']
    return (a, b)
