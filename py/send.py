# -*- coding: utf-8 -*-
import pika, sys

message = ' '.join(sys.argv[1:]) or 'Hello World'
# create a (TCP) connection, whose parameter use RabbitMQ Server's IP or name
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create a channel in that connection
channel = connection.channel()
# create a queue named 'hello', both Producer and Consumer should try to create channels
channel.queue_declare(queue='demo_queue', durable=True)  # make message persistent
# Producer can only send messages to exchanges
# set exchange name, routing key, and messages to send
# exchange will bind to queue
channel.basic_publish(
    exchange='',
    routing_key='demo_queue',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
print(" [x] Sent '%s'" % message)
# close connection
connection.close()

