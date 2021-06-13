from celery import Celery
app = Celery('add_tasks', broker='redis://192.168.98.142:6379/1', backend='redis://192.168.98.142:6379/2')
app.conf.update(
   #  配置所在时区
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    #  官网推荐消息序列化方式为json
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
   # 配置定时任务
    CELERYBEAT_SCHEDULE={
        'my_task': {
            'task': 'celery_beat.add',  # tasks.py模块下的add方法
            'schedule': 60,      # 每隔60运行一次
            'args': (23, 12),
        }
    }
)
@app.task
def add(x, y):
    return x + y