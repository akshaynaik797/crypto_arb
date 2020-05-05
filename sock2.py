import json, time
from pprint import pprint

from websocket import create_connection
ws = create_connection("wss://real.OKEx.com:8443/ws/v3")

b = '{"op": "subscribe", "args": ["spot/ticker:ETH-USDT"]}'
ws.send(json.dumps(b))

while True:
    result = ws.recv()
    result = json.loads(result)
    pprint(result)
ws.close()
