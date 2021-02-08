from gevent import monkey
monkey.patch_all()

from resource import app,init_app

import logging
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

logger = logging.getLogger('app')



@app.errorhandler(404)
def error_handle(error):
    return 'ERROR', 404



if __name__ == '__main__':
    logger.info('start webserver ...')
    init_app(app)
    http_server = WSGIServer(('0.0.0.0', 8888), app, handler_class=WebSocketHandler)
    logger.info('start listen 8888')
    http_server.serve_forever()


