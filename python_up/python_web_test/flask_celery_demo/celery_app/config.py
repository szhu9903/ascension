
import datetime

CELERY_RESULT_BACKEND = 'redis://:1017@127.0.0.1:6379/2'
BROKER_URL = 'amqp://szhu:szhu@47.102.40.50:5672/szhu_data'

CELERYBEAT_SCHEDULE = {
    'add-every-minute' : {
        'task' : 'flask_app.schedule.tasks.schedule_tasks',
        'schedule' : datetime.timedelta(minutes=1)
    }
}

CELERY_TIMEZONE='Asia/Shanghai'