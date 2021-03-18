import websocket
import json
# 须下载安装websocket-client依赖

url = "ws://127.0.0.1:8005/test/conn/"
ws = websocket.create_connection(url=url)
test_data = {
    "req_info":{
        "data":{
            "name":"szhu",
            "address":"上海市"
        }
    }
}

ws.send(json.dumps(test_data).encode('utf-8'))
print(ws.recv())
ws.close()

