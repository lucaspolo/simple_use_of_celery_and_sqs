import time

import cachelock
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task(queue='test-celery')
@cachelock.once(
    key='add-{x}-{y}',
    raise_if_lock=True
)
def add(x, y):
    return x + y


@app.task(queue='test-celery')
def agendado():
    f = open('tasks.txt', 'a')
    f.write('Execução agendada\n')
    f.close()
