import time
from arb_assets import fetch_bitbns_prices, check_for_triarb
while(1):
    try:
        prices = fetch_bitbns_prices()
        timestamp = time.time()
        with open("bitbns.csv", "a") as fp:
            fp.write(f"{timestamp}, {prices}"+'\n')
        time.sleep(1)
        var = 10
    except:
        print(f"error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
