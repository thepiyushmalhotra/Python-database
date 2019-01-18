import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Python"
)
mycursor = mydb.cursor()
sql = "UPDATE student SET name = 'Canyon' WHERE name = 'ac'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected") 
