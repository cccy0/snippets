import pika

# 连接队列服务器
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials(username="root", password="123456")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.98.143', credentials=credentials))
channel = connection.channel()

# 广播类型的交换机
# exchange 分为direct topic Fanout headers等类型

# topic就是模糊匹配
topic_exchange_name = 'topic_hello_exchange'
channel.exchange_declare(topic_exchange_name,
                         exchange_type=ExchangeType.topic,durable=True)
channel.basic_publish(topic_exchange_name, routing_key='topic.fffff', body=b'fuck you all topic')
print(" [x] Sent 'fuck you!'")


# direct routing key==binding key
# direct_exchange_name = 'direct_hello_exchange'
# channel.exchange_declare(direct_exchange_name,
#                          exchange_type=ExchangeType.direct)
# channel.basic_publish(direct_exchange_name, routing_key='my_direct_routing_key', body=b'fuck you all direct')
# print(" [x] Sent 'fuck you!'")


# fanout 忽略key对比 发送到所有的绑定到此exchange的queue routing_key为''
# fanout_exchange_name = 'fanout_hello_exchange'
# channel.exchange_declare(fanout_exchange_name,
#                          exchange_type=ExchangeType.fanout)
# channel.basic_publish(fanout_exchange_name, routing_key='', body=b'fuck you all fanout')
# print(" [x] Sent 'fuck you!'")

connection.close()
