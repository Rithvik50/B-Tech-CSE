import mysql.connector
import pika
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

# Define the queue name for this consumer
queue_name = 'itemcreation'

# Declare the queue
channel.queue_declare(queue=queue_name)

def callback(ch, method, properties, body):
    msg = body.decode()
    data = msg.split(' ')
    print(f" [x] Received {data}")

    if len(data) == 1:
        health_check_callback(ch, method, properties, body)
        return 

    conn = mysql.connector.connect(
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        host="database",
    )
    curr = conn.cursor()

    if len(data) == 2:
        curr = conn.cursor(buffered=True)
        curr.execute("select quantity from inventory where product_id=%s", (int(data[0]),))
        a = curr.fetchone()
        b=int(a[0])
        c=b+int(data[1])
        curr.execute("update inventory set quantity=%s where product_id=%s",(c,int(data[0]),))
        conn.commit()

    elif len(data)==3:
        curr.execute('delete from inventory where product_id=%s',(int(data[0]),))
        conn.commit()
    else:
        curr.execute("insert into inventory (product_name,quantity,unit_price,location) values (%s,%s,%s,%s)", (data[0], int(data[1]), float(data[2]), data[3]))
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
