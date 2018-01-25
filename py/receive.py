# -*- coding: utf-8 -*-
import pika

# create a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create a channel
channel = connection.channel()
# declare a queue(Consumer)
channel.queue_declare(queue='demo_queue', durable=True)

# define a callback function to handle received data
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# receive message from specified queue
channel.basic_consume(callback, queue='demo_queue', no_ack=True)
# loop for listening queue
print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()



