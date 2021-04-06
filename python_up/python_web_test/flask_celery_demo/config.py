from os.path import abspath, dirname
from datetime import timedelta

basedir = abspath(dirname(__file__))

class BaseConfig():
    SECRET_KEY = '5a8rGdvaf6f8g5d3787^Ml_d161'
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)

class DevConfig(BaseConfig):
    DEBUG = True

class RunConfig(BaseConfig):
    DEBUG = False


config_dict = {
    'dev': DevConfig,
    'run': RunConfig
}
