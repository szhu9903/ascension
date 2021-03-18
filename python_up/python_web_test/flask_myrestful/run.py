from gevent import monkey
monkey.patch_all()

from resource import create_app

import logging
import click
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

logger = logging.getLogger('app')

@click.command()
@click.option('--name', default='dev', help='Test flask name')
def run_app(name):
    logger.info('start webserver %s ...' % name)
    app = create_app(name)
    http_server = WSGIServer(('0.0.0.0', 8888), app, handler_class=WebSocketHandler)
    logger.info('start listen 8888')
    http_server.serve_forever()


if __name__ == '__main__':
    run_app()
    # logger.info('start webserver ...')
    # app = create_app()
    # http_server = WSGIServer(('0.0.0.0', 8888), app, handler_class=WebSocketHandler)
    # logger.info('start listen 8888')
    # http_server.serve_forever()


