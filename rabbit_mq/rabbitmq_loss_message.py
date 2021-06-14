import pika

# 连接队列服务器
from pika.exchange_type import ExchangeType

credentials = pika.PlainCredentials(username="root", password="123456")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.98.145', credentials=credentials))
channel = connection.channel()


topic_exchange_name = 'topic_hello_exchange'
# 1exchange 声明持久化
channel.exchange_declare(topic_exchange_name,
                         exchange_type=ExchangeType.topic,durable=True)
# 2队列声明持久化
#
# 3 消息持久化
# 虽然exchange和queue都声明了持久化，但是消息只存在内存里，rabbitmq重启后，内存里面的东西还是会丢失。所以必须声明消息也是持久化，从内存转存到硬盘。
# https://www.cnblogs.com/wangcuican/p/12124475.html
channel.basic_publish(topic_exchange_name, routing_key='topic.fffff', body=b'fuck you all topic',
                      properties=pika.BasicProperties(delivery_mode=2))
print(" [x] Sent 'fuck you!'")

connection.close()
