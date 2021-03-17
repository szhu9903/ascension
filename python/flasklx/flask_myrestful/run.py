from gevent import monkey
monkey.patch_all()

from resource import create_app

import logging
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

logger = logging.getLogger('app')





if __name__ == '__main__':
    logger.info('start webserver ...')
    app = create_app('dev')
    http_server = WSGIServer(('0.0.0.0', 8888), app, handler_class=WebSocketHandler)
    logger.info('start listen 8888')
    http_server.serve_forever()


