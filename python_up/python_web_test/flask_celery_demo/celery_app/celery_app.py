
from celery import Celery

# include 参数是程序启动时倒入的模块列表，可以该处添加任务模块
app = Celery('celery_app',
             include=['celery_app.tasks'])

app.config_from_object('celery_app.config')

