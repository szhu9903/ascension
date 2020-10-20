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
    web_socket = request.environ.get('wsgi.websocket')
    logger.info('websocket --> %s'%web_socket)
    if not web_socket:
        return "only connect"

    while not web_socket.closed:
        # 监听链接,接收数据
        msg = web_socket.receive()
        print(msg)
        web_socket.send(msg + 'youtoo')

    logger.info('close websocket')
    return 'close websocket'



if __name__ == '__main__':
    logger.info('start websocket')
    http_server = WSGIServer(('0.0.0.0', 5001), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
