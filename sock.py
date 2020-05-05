import json, time
from pprint import pprint

from websocket import create_connection
ws = create_connection("wss://fstream.binance.com/ws")


b = {"method": "SUBSCRIBE",
     "params":
    [
     "btcusdt@bookTicker",
    ],
     "id": 1
}

ws.send(json.dumps(b))

while True:
    result = ws.recv()
    result = json.loads(result)
    pprint(result)
ws.close()
