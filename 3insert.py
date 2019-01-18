import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Python"
)
mycursor = mydb.cursor()
a=input("Enter Name:")
b=input("Enter Address:")
c=input("Enter Phone:")
sql = "INSERT INTO student (name, address, Phone) VALUES (%s, %s, %s)"
val = (a,b,c)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
