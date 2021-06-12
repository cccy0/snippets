from celery import Celery

broker_url='redis://@192.168.98.140/'
app = Celery('hello', backend='rpc://',broker=broker_url)


@app.task
def add(x, y):
    return x + y

# workers
# celery -A tasks worker --loglevel=INFO

