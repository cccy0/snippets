import pika
from pika import exceptions as pika_exceptions
# 连接队列服务器
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials(username="root", password="123456")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.98.145', credentials=credentials))
channel = connection.channel()

channel.confirm_delivery()
# 广播类型的交换机
# exchange 分为direct topic Fanout headers等类型

# topic就是模糊匹配
topic_exchange_name = 'topic_hello_exchange'
channel.exchange_declare(topic_exchange_name,
                         exchange_type=ExchangeType.topic,durable=True)
try:
    channel.basic_publish(topic_exchange_name, routing_key='topic.fffff', body=b'fuck you all topic')
    print('message confirmed')
    #
except pika_exceptions.UnroutableError as e:
    print('message not confirmed')


print(" [x] Sent 'fuck you!'")



connection.close()
