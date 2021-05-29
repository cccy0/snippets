import pika

# 连接队列服务器
credentials=pika.PlainCredentials(username="root",password="123456")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.98.130',credentials=credentials))
channel = connection.channel()

# 创建队列。有就不管，没有就自动创建
channel.queue_declare(queue='hello')

# 使用默认的交换机发送消息。exchange为空就使用默认的
channel.basic_publish(exchange='hello', routing_key='hello', body=b'fuck you all')
print(" [x] Sent 'fuck you!'")
connection.close()
