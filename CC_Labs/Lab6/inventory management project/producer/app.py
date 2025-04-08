from flask import Flask, session, render_template, request, redirect, url_for
import mysql.connector
import os
import pika
app = Flask(__name__)
app.secret_key = '123456789'

MYSQL_USER = "myuser"
MYSQL_PASSWORD = "password"
MYSQL_DATABASE = "mydatabase"

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        user="myuser",
        password="password",
        host="database",
        database="mydatabase",
    )


# Connection parameters for RabbitMQ running inside Docker container
rabbitmq_host = 'rabbitmqcontainer'
rabbitmq_port = 5672
rabbitmq_user = 'user'
rabbitmq_pass = "password"

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

print("Connected to RabbitMQ")

    # Define the queue names for this producer
queue_names = ['healthcheck', 'stockmanagement', 'orderprocessing', 'itemcreation']

for queue_name in queue_names:
        # Declare a queue
    channel.queue_declare(queue=queue_name)

connection.close()

def Itemcreation(msg):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='itemcreation',body=msg)
    print("sucessfully sent")
    connection.close()

# msg='6 sdf frt'
# Itemcreation(msg)

def Stockmanagement(msg):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='stockmanagement',body=msg)
    print("sucessfully sent")
    connection.close()

def Orderprocessing(msg):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='orderprocessing',body=msg)
    print("sucessfully sent")
    connection.close()

def Healthcheck(msg):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    parameters = pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.basic_publish(exchange='',routing_key='healthcheck',body=msg)
    print("sucessfully sent")
    connection.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_type = request.form['user_type']

        conn = get_db_connection()
        c = conn.cursor(buffered=True)

        if user_type == 'user':
            c.execute("SELECT * FROM users WHERE name=%s AND password=%s", (name, password))
            user = c.fetchone()
            if user:
                session['user_id'] = user[0]
                session['name'] = name
                session['user_type'] = 'user'
                return redirect(url_for('dashboard'))
        elif user_type == 'admin':
            c.execute("SELECT * FROM admins WHERE name=%s AND password=%s", (name, password))
            admin = c.fetchone()
            if admin:
                session['admin_id'] = admin[0]
                session['name'] = name
                session['user_type'] = 'admin'
                return redirect(url_for('admin'))

        conn.close()
        c.close() 
        return render_template('index.html', error='Invalid credentials')

    return render_template('index.html')



@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html', user_type=session.get('user_type'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'user_type' not in session or session['user_type'] != 'admin':
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST' and request.form:
        action = request.form.get('action')

        if action == 'add_item':
            product_name = request.form['product_name']
            quantity = request.form['quantity']
            unit_price = request.form['unit_price']
            location = request.form['location']
            msg=product_name+' '+quantity+' '+unit_price+' '+location
            Itemcreation(msg)
            return redirect(url_for('admin'))  # Redirect to the same route after adding an item

    cursor.execute('SELECT * FROM inventory')
    inventory = cursor.fetchall()

    cursor.execute("SELECT order_id, userid, productname, quantity, price, stats FROM orders")
    orders = cursor.fetchall()

    conn.close()

    return render_template('admin.html', inventory=inventory, orders=orders)


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        product_ids = request.form.getlist('item_id[]')
        product_name = request.form.getlist('product_name[]')
        quantities = request.form.getlist('quantity[]')
        print(product_ids)
        
        msg=product_name[0]+' '+quantities[0]+' '+ str(session['user_id'])
        Stockmanagement(msg)
        return redirect(url_for('order_history'))

    else:
        return render_template('buy.html', inventory=get_inventory())

def get_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT product_id, product_name, unit_price, quantity FROM inventory")
    inventory = cursor.fetchall()
    conn.close()
    return inventory

@app.route('/order_history')
def order_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT order_id,productname,quantity,price,stats FROM orders WHERE userid = %s", (session['user_id'],))

    orders = cursor.fetchall()
    print(orders)
    conn.close()

    return render_template('order_history.html', orders=orders)

@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        products_id = request.form.get('product_id')
        if(products_id==None):
            cursor.execute("SELECT product_id, product_name, quantity FROM inventory")
            inventory = cursor.fetchall()
            conn.close()
            return render_template('addstocks.html', inventory=inventory)
            
        add_quantity = request.form.get('add_quantity')  # Default is zero if not provided
        print(f"productsid {products_id}")
        asd="gh"
        if(type(products_id)!=type(asd)):
            products_id=str(products_id)
        msg=products_id+' '+ add_quantity
        print(msg)
        Itemcreation(msg)
        
        return redirect(url_for('add_stock'))  # Redirect back to see the updated results

    # For GET requests, fetch current inventory data
    cursor.execute("SELECT product_id, product_name, quantity FROM inventory")
    inventory = cursor.fetchall()
    conn.close()
    return render_template('addstocks.html', inventory=inventory)

@app.route('/update_status', methods=['POST'])
def update_status():
    if 'user_id' not in session or session.get('user_type') != 'admin':
        return redirect(url_for('login'))

    order_id = request.form['order_id']
    new_status = request.form['status']

    msg=order_id+' '+new_status
    Itemcreation(msg)
    

    return redirect(url_for('admin'))


# @app.route('/Delete_Product',methods=['GET'])
# def Delete_Product():
#     if 'user_id' not in session or session.get('user_type') != 'admin':
#         return redirect(url_for('login'))

#     product_id = request.form['product_id']
    

#     msg=product_id+' '+'jk'+' '+'kl';
#     Orderprocessing(msg)
    

#     return redirect(url_for('admin'))


@app.route('/Delete_Product', methods=['POST', 'GET'])
def Delete_Product():
    # For testing: Directly set session variables
    session['user_id'] = 1  # Example user ID
    session['user_type'] = 'admin'
    if 'user_id' not in session or session.get('user_type') != 'admin':
        return redirect(url_for('login'))

    product_id = request.form.get('product_id')
    if not product_id:
        return redirect(url_for('admin'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE product_id=%s", (product_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/health_check', methods=['GET'])
def health_check():
    # For testing: Directly set session variables
    session['user_id'] = 1  # Example user ID
    session['user_type'] = 'admin'
    Healthcheck('1')
    if 'user_id' not in session or session.get('user_type') != 'admin':
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM health')
    healthcheck = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('healthcheck.html', healthcheck=healthcheck)

@app.route('/success')
def success():
    return render_template('dashboard.html')

if __name__ == '__main__':
    print("in main trying to render")
    
    
    app.run(debug=True)
