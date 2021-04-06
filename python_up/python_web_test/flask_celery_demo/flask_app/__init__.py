from os import getenv
from flask import Flask
from config import config_dict

def create_app(config_dev):
    app = Flask(__name__)
    if not config_dev:
        config_dev = getenv('FLASK_ENV', 'dev')
    app.config.from_object(config_dict[config_dev])
    register_blueprint_helper(app)    # 加载蓝图及中间件
    return app


def register_blueprint_helper(app):
    from .main import main
    app.register_blueprint(main, url_prefix='/main')


import celery
def make_celery(app):
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery

