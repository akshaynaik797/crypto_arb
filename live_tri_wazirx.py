import requests, os
from time import sleep
from tri_wazirx import pairs, check_for_triarb
var = 10
url1 = "https://api.wazirx.com/api/v2/tickers"
while(1):
        data = requests.get(url1).json()
        try:
            for pair in pairs:
                if check_for_triarb(pair, data, limit=1.006):
                    print(pair)
                    os.system('paplay chimes-glassy.ogg &')
            sleep(30)
            var = 10
        except Exception as error:
            print(error, f"wait {var} seconds.")
            sleep(var)
            var = var*1.5
