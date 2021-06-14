import functools
import logging
from datetime import datetime

import pika
import threading
import time


#
# LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
#               '-35s %(lineno) -5d: %(message)s')
# LOGGER = logging.getLogger(__name__)
#
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


def ack_message(channel, delivery_tag):
    """Note that `channel` must be the same pika channel instance via which
    the message being ACKed was retrieved (AMQP protocol constraint).
    """
    print('ack')
    if channel.is_open:
        channel.basic_ack(delivery_tag)
    else:
        # Channel is already closed, so we can't ACK this message;
        # log and/or do something that makes sense for your app in this case.
        pass

# 还可以在搞队列 设置队列，主线程就是添加队列元素 子线程就是干活
# 防止消息过多 可以事先开好线程池 子线程从队列中去元素
# 防止队列过大 可以设置大小 然后block 超时了就pass
def do_work(connection, channel, delivery_tag, body):
    thread_id = threading.get_ident()
    fmt1 = 'Thread id: {} Delivery tag: {} Message body: {}'
    print(fmt1.format(thread_id, delivery_tag, body), datetime.now())
    # Sleeping to simulate 10 seconds of work
    time.sleep(181)
    print('消费完了')
    cb = functools.partial(ack_message, channel, delivery_tag)
    connection.add_callback_threadsafe(cb)


def on_message(channel, method_frame, header_frame, body, args):
    print('3424')
    # time.sleep(181)
    print('fky')
    (connection, threads) = args
    delivery_tag = method_frame.delivery_tag
    t = threading.Thread(target=do_work, args=(connection, channel, delivery_tag, body))
    t.start()
    threads.append(t)


credentials = pika.PlainCredentials('root', '123456')
# Note: sending a short heartbeat to prove that heartbeats are still
# sent even though the worker simulates long-running work
parameters = pika.ConnectionParameters(host='192.168.98.143', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
# channel.exchange_declare(exchange="hello", exchange_type="direct", passive=False, durable=True, auto_delete=False)
# channel.exchange_declare(exchange="hello",)
# channel.queue_declare(queue="hello", auto_delete=False)
channel.queue_declare(queue="hello", )
# channel.queue_bind(queue="hello", exchange="hello", routing_key="hello")
# Note: prefetch is set to 1 here as an example only and to keep the number of threads created
# to a reasonable amount. In production you will want to test with different prefetch values
# to find which one provides the best performance and usability for your solution
# channel.basic_qos(prefetch_count=10)

threads = []
on_message_callback = functools.partial(on_message, args=(connection, threads))
channel.basic_consume(on_message_callback=on_message_callback, queue='hello', auto_ack=False)

try:

    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

# Wait for all to complete
for thread in threads:
    thread.join()

connection.close()
