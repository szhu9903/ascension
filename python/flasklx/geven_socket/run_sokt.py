import logging
from flask import Flask
from flask import request
from geventwebsocket import WebSocketError
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
logger = logging.getLogger('app')


@app.route('/conn')
def index():
    #获取请求原始数据
    user_socket = request.environ
    #获取websocket对象
    websocket_obj = user_socket['wsgi.websocket']

    while True:
        # 监听链接,接收数据
        msg = websocket_obj.receive()
        print(msg)
        websocket_obj.send(msg + 'youtoo')



if __name__ == '__main__':
    logger.info('start websocket')
    http_server = WSGIServer(('0.0.0.0', 8005), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
