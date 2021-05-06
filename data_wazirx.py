import requests, time
var = 10 
record = {}
url1 = "https://api.wazirx.com/api/v2/tickers"
while(1):
    try:
        data = requests.get(url1)
        data = data.json()
        timestamp = time.time()
        if data != record:
            record = data
            with open("wazirx.csv", "a") as fp:
                row = f"{timestamp}|{record}\n"
                fp.write(row)
        time.sleep(1)
        var = 10
    except:
        print(f"error wait {var} seconds.")
        time.sleep(var)
        var = var*1.1
