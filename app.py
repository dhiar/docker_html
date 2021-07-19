import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Docker Update Dhiar!'

@app.route('/widgets')
def get_widgets() :
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="manager247",
    database="inventory"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="manager247"
  )
  mycursor = mydb.cursor()
  mycursor.execute("DROP DATABASE IF EXISTS inventory")
  mycursor.execute("CREATE DATABASE inventory")
  mydb.commit()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="manager247",
    database="inventory"
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE widgets (id int NOT NULL AUTO_INCREMENT, name VARCHAR(255), description VARCHAR(255), PRIMARY KEY (id))")
  mydb.commit()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="manager247",
    database="inventory"
  )
  mycursor = mydb.cursor()
  
  sql = "INSERT INTO widgets (name, description) VALUES (%s, %s)"
  val = [
    ("widgets_1", "description_1"),
    ("widgets_2", "description_2")
  ]
  mycursor.executemany(sql, val)

  mydb.commit()
  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
