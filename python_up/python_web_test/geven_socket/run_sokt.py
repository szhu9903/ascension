import logging
import json
from flask import Flask, request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

# 初始化日志
applog = logging.getLogger('app')
applog.setLevel(logging.DEBUG)

appHandler = logging.StreamHandler()
appFormatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S")
appHandler.setLevel(logging.DEBUG)
appHandler.setFormatter(appFormatter)
applog.addHandler(appHandler)



app = Flask(__name__)

@app.route('/test/conn/')
def test_conn():
    web_socket = request.environ.get("wsgi.websocket")
    if not web_socket:
        return "ERROE NOT SOCKET"
    while not web_socket.closed:
        ws_message = web_socket.receive()
        if not ws_message:
            break
        else:
            logger.info(json.loads(ws_message))
            web_socket.send('HI ')
    logger.info('close websocket(syncfunc)')
    return 'close websocket(syncfunc)'



if __name__ == '__main__':
    logger = logging.getLogger('app')
    logger.info("Start New Websocket")
    http_server = WSGIServer(('0.0.0.0', 8005), app, handler_class = WebSocketHandler)
    http_server.serve_forever()