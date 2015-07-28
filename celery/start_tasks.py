from celery import Celery
from eurpy import fib as _fib
BROKER_URL = 'redis://yippy.local:6379/0' #Use database 0 on yippy.local
CELERY_RESULT_BACKEND = 'redis://yippy.local:6379/0'
app = Celery('tasks', backend=CELERY_RESULT_BACKEND, broker=BROKER_URL)

@app.task()
def fib(n)
    return _fib(n)

@app.task()
def echo(msg)
    return msg
#Command line: celery -A tasks -c 4 -l info worker
#Mirar para workers, Condor Job