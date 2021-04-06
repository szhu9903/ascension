
from celery_app.celery_app import app
import time

@app.task
def add_longtime(a, b):
    print ('long time task begins')
    time.sleep(3)
    print ('long time task finished')
    return a + b