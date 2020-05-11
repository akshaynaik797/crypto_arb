import requests, os
from time import sleep
from tri_bitbns import pairs, check_for_triarb
var = 10
url1 = "https://bitbns.com/order/getTickerWithVolume/"
while(1):
        data = requests.get(url1).json()
        try:
            for pair in pairs:
                if check_for_triarb(pair, data):
                    print(pair)
                    os.system('paplay chimes-glassy.ogg &')
            sleep(60)
            var = 10
        except Exception as error:
            print(error, f"wait {var} seconds.")
            sleep(var)
            var = var*1.5
