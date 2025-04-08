import pika
import mysql.connector
import os
# Connection parameters for RabbitMQ running inside Docker container
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

# Define the queue name for this consumer
queue_name = 'orderprocessing'


def callback(ch, method, properties, body):
    msg=body.decode();
    data=msg.split(' ')  
    
    if(len(data)==1):
        health_check_callback(ch, method, properties, body)
        return 

    conn = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        host="database",
    )
    curr=conn.cursor()

           #msg=orderid

    curr.execute('update orders set stats=%s where order_id=%s',(data[1],int(data[0])))
    conn.commit()

    curr.close()
    conn.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)

def health_check_callback(ch, method, properties, body):
    conn = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        host="database",
    )
    curr=conn.cursor()
    curr.execute("update health set stat=%s where containername=%s",("Active",queue_name))
    conn.commit()

    curr.close()
    conn.close()
    ch.basic_ack(delivery_tag=method.delivery_tag)  

# Subscribe to the queue and consume messages
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
