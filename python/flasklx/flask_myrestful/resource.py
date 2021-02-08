
import logging
applog = logging.getLogger('app')
applog.setLevel(logging.DEBUG)
appHandle = logging.StreamHandler()
appHandle.setLevel(logging.DEBUG)
appHandle.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"))
applog.addHandler(appHandle)


import sys
env = sys.argv[1]
if env == 'local':
    from config.dev_config import *
elif env == 'run':
    from config.run_config import *



from datetime import timedelta
from flask import Flask
from comm import helper



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.json_encoder = helper.JSONEncoder


def init_app(application):
    application.config['DEBUG'] = DEBUG
    application.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
    # 注册蓝图
    from api.requestController import main
    application.register_blueprint(main, url_prefix='/api/zsj/main')

