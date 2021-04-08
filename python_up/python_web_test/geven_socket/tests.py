
import unittest
from websocket import create_connection

"""
from websocket import create_connection

ws_url = 'ws://127.0.0.1:8005/wsmsg/conn/'
ws_server = create_connection(ws_url)

while True:
    message = input('send data: ')
    ws_server.send(message)
    recv_data = ws_server.recv()
    print(recv_data)
"""

class SocketTest(unittest.TestCase):
    def setUp(self):
        self.ws_url = "ws://127.0.0.1:8005/wsmsg/conn/"
        self.ws_server = create_connection(self.ws_url)

    def test_send(self):
        # 发送数据
        self.ws_server.send('hello test gevent websocket')
        # 获取数据
        res_data = self.ws_server.recv()
        self.assertTrue(res_data)
        print(res_data)






