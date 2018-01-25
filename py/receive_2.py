# -*- coding: utf-8 -*-
import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='demo_queue', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep(body.count('.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# qos - quality of service
# Fair dispatch, balance each consumer's load
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback, queue='demo_queue')
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()