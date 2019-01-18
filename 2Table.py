import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="python"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE student (name VARCHAR(255), address VARCHAR(255), Phone int)")
