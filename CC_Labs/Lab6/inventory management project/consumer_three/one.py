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
queue_name = 'stockmanagement'


def callback(ch, method, properties, body):
    msg=body.decode();          # productname 5 userid'
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
    curr.execute('select product_id,quantity,product_name,unit_price from inventory where product_name=%s order by quantity desc',(data[0],))
    tabledata=curr.fetchall()
    print(tabledata)
    print(data)
    if(int(tabledata[0][1])<int(data[1])):
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    else:
        curr.execute('update inventory set quantity=%s where product_id=%s',(int(tabledata[0][1])-int(data[1]),tabledata[0][0],))
        curr.execute('insert into orders (userid,productname,quantity,price,stats) values (%s,%s,%s,%s,%s)',(int(data[2]),data[0],int(data[1]),float(float(tabledata[0][3])*int(data[1])),'pending',))
        conn.commit()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    curr.close()
    conn.close()
    
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