import logging
import json
from flask import Flask, request, render_template
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


app = Flask(__name__,
            template_folder='./templates')
users = set()

@app.route('/')
@app.route('/index')
def index():
    return render_template('sokt_h.html')

@app.route('/wsmsg/conn/')
def test_conn():
    # 获取Web Socket连接
    web_socket = request.environ.get("wsgi.websocket")
    if not web_socket:
        return "ERROE NOT SOCKET"
    # 连接加入链接池中
    users.add(web_socket)
    while not web_socket.closed:
        ws_message = web_socket.receive()
        if ws_message == 'exit': break
        logger.info('现有用户%s' % len(users))
        for user in users:
            try:
                user.send(ws_message)
            except Exception as er:
                print('用户断开')
    users.remove(web_socket)
    logger.info('close websocket(syncfunc)')
    return 'close websocket(syncfunc)'



if __name__ == '__main__':
    logger = logging.getLogger('app')
    logger.info("Start New Websocket")
    http_server = WSGIServer(('0.0.0.0', 8005), app, handler_class = WebSocketHandler)
    http_server.serve_forever()