from celery import Celery

broker_url='redis://@192.168.98.142:6379/1'
backend_url='redis://@192.168.98.142:6379/2'
# app = Celery('hello', backend='rpc://',broker=broker_url)
app = Celery('hello', backend=backend_url,broker=broker_url)


@app.task
def add(x, y):
    return x + y

# celery是分布式任务调度工具
# celery启动worker -A 表示加载Celery对象的模块


