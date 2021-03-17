
import logging
applog = logging.getLogger('app')
applog.setLevel(logging.DEBUG)
appHandle = logging.StreamHandler()
appHandle.setLevel(logging.DEBUG)
appHandle.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"))
applog.addHandler(appHandle)

import os
from flask import Flask
from config.base_config import config
from comm import helper
from comm.db import register_db_helper
from comm.extensions import login_message



def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])    # 获取配置文件
    app.json_encode = helper.JSONEncoder    # 加载辅助日志及JSON设置
    register_db_helper(config[config_name].db_conf)    # 初始化数据库链接池
    register_extensions_helper(app)    # 加载扩展
    register_blueprint_helper(app)    # 加载蓝图及中间件
    register_error_helper(app)

    return app

# 加载扩展
def register_extensions_helper(app):
    login_message.init_app(app)

# 加载中间件、蓝图
def register_blueprint_helper(app):
    from comm.middles import middle
    middle(app)
    from api.requestController import main
    app.register_blueprint(main, url_prefix = '/api/zsj/main')
    from api.userController import user
    app.register_blueprint(user, url_prefix = '/api/zsj/user')

# 错误视图处理
def register_error_helper(app):
    @app.errorhandler(400)
    def error_request(e):
        return e, 400
