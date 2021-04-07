from celery_app.celery_app import app
import datetime

@app.task
def schedule_task(*args, **kwargs):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)