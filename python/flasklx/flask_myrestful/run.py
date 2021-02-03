from gevent import monkey
monkey.patch_all()

import logging
import json
from comm import utilConfig
from comm import helper
from flask import Flask
from datetime import timedelta
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

logger = logging.getLogger('app')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5a8rGdvaf6f8g5d3787^Ml_d161'
app.json_encoder = helper.JSONEncoder

@app.errorhandler(404)
def error_handle(error):
    return 'ERROR', 404

def init_app(application):
    application.config['DEBUG'] = True
    application.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
    # 注册蓝图
    from api.requestController import main
    application.register_blueprint(main, url_prefix='/api/zsj/main')

if __name__ == '__main__':
    logger.info('start webserver ...')
    init_app(app)
    http_server = WSGIServer(('0.0.0.0', 8888), app, handler_class=WebSocketHandler)
    logger.info('start listen 8888')
    http_server.serve_forever()


