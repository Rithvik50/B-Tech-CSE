import mysql.connector
import pika
import time
import os

rabbitmq_host = 'rabbitmqcontainer'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = "password"

# Establish connection to RabbitMQ
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


MYSQL_USER = "myuser"
MYSQL_PASSWORD = "password"
MYSQL_DATABASE = "mydatabase"
  # Default to container name

queue_name = 'healthcheck'

def send_health_check_message(consumer_name):
    try:
        channel.basic_publish(exchange='', routing_key=consumer_name, body='Health')
        print(f"Health check message sent to consumer: {consumer_name}")
    except Exception as e:
        print("Failed to send health check:", e)

def send_health_check(ch, method, properties, body):
    consumers = ['stockmanagement', 'orderprocessing', 'itemcreation']
    conn = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        host="database",
        
    )
    curr = conn.cursor()
    for i in consumers:
        curr.execute("update health set stat=%s where containername=%s", ("Not Active", i))
    conn.commit()

    curr.close()
    conn.close()
    for consumer in consumers:
        send_health_check_message(consumer)
    
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name, on_message_callback=send_health_check, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
