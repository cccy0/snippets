import pika
from pika.exchange_type import ExchangeType

auth = pika.PlainCredentials('root', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.98.143', credentials=auth))
channel = connection.channel()

queue_name = 'hello'
channel.queue_declare(queue=queue_name,durable=True)

exchange_name = 'topic_hello_exchange'
channel.exchange_declare(
    exchange=exchange_name,
    exchange_type=ExchangeType.topic,
    durable=True
)

# queue绑定到exchange
channel.queue_bind(
    exchange=exchange_name,
    queue=queue_name,
    routing_key='topic.#'
)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body,method.routing_key)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback,
                      queue='hello',
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
# https://blog.csdn.net/qq_41993287/article/details/107492441