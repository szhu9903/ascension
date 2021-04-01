
from celery import Celery
from .config import *

# include 参数是程序启动时倒入的模块列表，可以该处添加任务模块
app = Celery('celery_demo',
             include=['celery_demo.tasks'])

app.config_from_object('celery_demo.config')

