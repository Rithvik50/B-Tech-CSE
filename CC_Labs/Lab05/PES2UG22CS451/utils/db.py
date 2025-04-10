import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

dbconfig = {
    "host": os.getenv("host"),
    "user": os.getenv("user"),
    "password": os.getenv("password"),
    "database": "notes"
}


cnx_pool=mysql.connector.pooling.MySQLConnectionPool(
    pool_name="notes",
    pool_size=10,
    **dbconfig
)

def connect_to_mysql():
   return cnx_pool.get_connection()

# def connect_to_mysql():
#     cnx=mysql.connector.connect(
#         **dbconfig
#     )
#     return cnx
def setup_database():
    cnx=connect_to_mysql()
    create_table="CREATE TABLE IF NOT EXISTS NOTES (id INT NOT NULL AUTO_INCREMENT, title VARCHAR(50) NOT NULL, content TEXT NOT NULL, PRIMARY KEY (id));"
    cursor=cnx.cursor()
    try:
        cursor.execute(create_table)
        print("Created table")
    except mysql.connector.Error as err:
        print("Error creating table", err)
        exit(1)
    finally:
        cursor.close()
        cnx.close()
    
        

def insert(title, content):
    cnx=connect_to_mysql()
     
    query="INSERT INTO NOTES (title, content) VALUES ('{}', '{}');".format(title, content)
    try:
        cursor=cnx.cursor()   
        cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        print("Error inserting row")
    finally:
        cursor.close()
        cnx.close()
    

    
def get_note(id=None):
    cnx=connect_to_mysql()
    if id is not None:    
        query="SELECT * FROM NOTES where id={}".format(id)
        try:
            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
            
        except mysql.connector.Error as err:
            print("Error fetching entry", err)
        finally:
            cursor.close()
            cnx.close()
    
    else:
        query="SELECT * FROM NOTES"
        try:
            cursor=cnx.cursor(dictionary=True)
            cursor.execute(query)
            return cursor.fetchall()
            
        except mysql.connector.Error as err:
            print("Error fetching entry")
        finally:
            cursor.close()
            cnx.close()
        
    
def update(id, title, content):
    cnx=connect_to_mysql()
    query = "UPDATE NOTES SET title = '{}', content = '{}' WHERE id = {};".format(title, content,int(id))
    
    try:
        cursor=cnx.cursor()
        cursor.execute(query)
        
        
        cnx.commit()
        
    except Exception as e:
        print("Error updating note",e)
    finally:
        cursor.close()
        cnx.close()
        
        
def delete(id):
    cnx=connect_to_mysql()
    query = "DELETE FROM NOTES WHERE id = {};".format(int(id))
    
    try:
        cursor=cnx.cursor()
        cursor.execute(query)
        cnx.commit()
        print("done")
        
    except Exception as e:
        print("Error updating note",e)
    finally:
        cursor.close()
        cnx.close()
        

